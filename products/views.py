from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from star_ratings.models import Rating

from .forms import ProductForm
from .models import Product, Category, PreviewImage
from profiles.models import UserProfile

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
            if sortkey == 'name_asc':
                products = products.annotate(lower_name=Lower('name')).order_by('lower_name')
            elif sortkey == 'name_desc':
                products = products.annotate(lower_name=Lower('name')).order_by('-lower_name')
            elif sortkey == 'category_asc':
                products = products.order_by('category__name')
            elif sortkey == 'category_desc':
                products = products.order_by('-category__name')
            elif sortkey == 'price_asc':
                products = products.order_by('price')
            elif sortkey == 'price_desc':
                products = products.order_by('-price')
            # elif sortkey == 'rating_asc':
            #     products = products.annotate(average_rating=Avg('ratings__score')).order_by('average_rating')
            # elif sortkey == 'rating_desc':
            #     products = products.annotate(average_rating=Avg('ratings__score')).order_by('-average_rating')           

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(category__name__icontains=query)
                | Q(category__friendly_name__icontains=query)
            )
            # distinct removes duplicate results
            products = products.filter(queries).distinct()

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
    in_wishlist = False
    show_wishlist = False
    
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        in_wishlist = profile.wish_list.filter(id=product.id).exists()
        show_wishlist = True

    if request.method == 'POST':
        score = request.POST.get('rating')

        if score:
            product.rating.add(score=int(score), user=request.user)
            messages.success(request, 'Thank you for your rating!')
        else:
            messages.error(request, 'Please select a rating.')


    context = {
        'product': product,
        'preview_images': preview_images,
        'in_wishlist': in_wishlist,
        'show_wishlist': show_wishlist,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """To add products"""

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
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.',
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def upload_product_view(request):
    message = None
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save()

            for img in request.FILES.getlist('images'):
                PreviewImage.objects.create(product=product, image=img)
            message = 'Product uploaded successfully!'
        else:
            messages.error(request, 'Failed to upload product. ')
    else:
        product_form = ProductForm()

    return render(
        request,
        'upload_product.html',
        {'product_form': product_form, 'message': message},
    )


@login_required
def edit_product(request, product_id):
    """Edit a product in the store products """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    preview_images = PreviewImage.objects.filter(product=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product_instance = form.save()

            for i in range(len(preview_images)):
                image_id = request.POST.get(f'previewimage_set-{i}-id')
                new_image = request.FILES.get(f'previewimage_set-{i}-image')
                
                if new_image:
                    preview_image = PreviewImage.objects.get(id=image_id)
                    preview_image.image = new_image
                    preview_image.save()

                if request.POST.get(f'previewimage_set-{i}-DELETE'):
                    PreviewImage.objects.filter(id=image_id).delete()


            images = request.FILES.getlist('images')
            for image in images:
                PreviewImage.objects.create(product=product_instance, image=image)

            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
        'preview_images': preview_images,
    }

    return render(request, 'products/edit_product.html', context)

@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

# @login_require
# def delete_image