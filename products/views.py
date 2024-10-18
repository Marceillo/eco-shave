from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
# from star_ratings.fields import RatingField
from star_ratings.models import Rating

from .forms import ProductForm
from.models import Product, Category, PreviewImage


def all_products(request):
    """
    For all products with some filtering ans sorting.
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    directions = 'asc'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name' 
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """
   Provides more information on the product.
    """
    product = get_object_or_404(Product, pk=product_id)
    preview_images = PreviewImage.objects.filter(product=product)
    
    for image in preview_images:
        print(image.image.url)

    if request.method == 'POST':
        score = request.POST.get('rating')

        if score:
            product.rating.add(score=int(score), 
            user=request.user)
            messages.success(request, 'Thank you for your rating!')
        else:
            messages.error(request, 'Please select a rating.')

    context = {
        'product': product,
        'preview_images': preview_images,
        # 'average_rating': average_rating,
         
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """  """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False) 
            product.save() 
            
            
            images = request.FILES.getlist('images')  
            for image in images:
                PreviewImage.objects.create(product=product, image=image)  
            
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def upload_product_view(request):
    message = None
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save()
            # Handling multiple images
            for img in request.FILES.getlist('images'):
                PreviewImage.objects.create(product=product, image=img)
            message = 'Product uploaded successfully!'
    else:
        product_form = ProductForm()
    
    return render(request, 'upload_product.html', {'product_form': product_form, 'message': message})
