from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages # messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    
      
    shopping_bag = request.session.get('shopping_bag', {})
    print("Shopping bag contents:", shopping_bag)  # Debugging
    total_items = sum(shopping_bag.values())
    total_price = sum(Product.objects.get(pk=int(item_id)).price * quantity for 
    item_id, quantity in shopping_bag.items())
    print("Total price calculated:", total_price)  # Debugging

    product_dict = {}

    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=int(item_id))
        product_dict[item_id] = {
            'product': product,
            'quantity': quantity,
        }

    context = {
        'shopping_bag': shopping_bag,
        'total_items': total_items,
        'total_price': total_price,
        'product_dict': product_dict,
        
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag( request, item_id):
    """
    Add products to the shopping bag. 
    """
   
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    shopping_bag = request.session.get('shopping_bag', {})

    item_id = str(item_id)
    if item_id in shopping_bag:
        shopping_bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {shopping_bag[item_id]}') 
    else:
        shopping_bag[item_id]= quantity
        messages.success(request, f'Added {product.name} to your bag.')

    request.session['shopping_bag'] = shopping_bag
    
    return redirect(reverse('view_bag'))
    
    def adjust_bag(request, item_id):
        """ Adjust the quantity of the specified product in the bag """
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity', 0))
        shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 0:
        shopping_bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {shopping_bag[item_id]}')
    else:
        if item_id in shopping_bag:
            del shopping_bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove a product from the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in shopping_bag:
        del shopping_bag[item_id]
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['shopping_bag'] = shopping_bag
    return HttpResponse(status=200)







