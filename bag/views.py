from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages # messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    shopping_bag = request.session.get('shopping_bag', {})

    context = {
        'items_in_bag_contents':
        sum(shopping_bag.values()),
        'shopping_bag': shopping_bag,

    }

    return render(request, 'bag/bag.html', context)


def add_to_bag( request, item_id):
    """
    Add products to the shopping bag. 
    """
    product = get_object_or_404(Product, pk=item_id)
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in shopping_bag:
        shopping_bag[item_id] += 1 
    else:
        shopping_bag[item_id]= 1
        request.session['shopping_bag'] = shopping_bag
        messages.success(request, f'Added {product.name} to your bag.') 






