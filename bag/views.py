from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages # messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    shopping_bag = request.session.get('shopping_bag', {})
    total_items = sum(shopping_bag.values())
    total_price = sum(Product.objects.get(pk=int(item_id)).price * quantity for 
    item_id, quantity in shopping_bag.items())
  
    context = {
        'shopping_bag': shopping_bag,
        'total_items': total_items,
        'total_price': total_price,
        
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag( request, item_id):
    """
    Add products to the shopping bag. 
    """
   
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    shopping_bag = request.session.get('bag', {})
   
    if item_id in shopping_bag:
        shopping_bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {shopping_bag[item_id]}') 
    else:
        shopping_bag[item_id]= quantity
        messages.success(request, f'Added {product.name} to your bag.')

    request.session['bag'] = shopping_bag
    
    return redirect(reverse('view_bag'))
 






