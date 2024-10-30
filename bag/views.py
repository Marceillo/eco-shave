from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


from bag.contexts import bag_contents

def view_bag(request):
    """
    A view that renders the shopping bag contents page
    """
    context = bag_contents(request)
    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id):
    """
    Add products to the shopping bag. 
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    item_id = str(item_id)
    if str(item_id) in shopping_bag:

        shopping_bag[str(item_id)] += quantity

        messages.success(request, f'Updated {product.name} quantity to {shopping_bag[item_id]}')
 
    else:
        shopping_bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag.')
        
    request.session['shopping_bag'] = shopping_bag
    
    return redirect(redirect_url)
   

def adjust_bag(request, item_id):
    """ 
    Adjust the quantity of the specified product in the bag
    
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag', {})
    action = request.POST.get('action')

    if quantity >= 0:
        shopping_bag[item_id] = quantity
        messages.success(request,
        f'Updated size {product.name} quantity to {shopping_bag[item_id]}',
        )
    else:
        # del shopping_bag[item_id]
        # if not shopping_bag[item_id]: 
        shopping_bag.pop(item_id) 
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_bag'))
    

def remove_from_bag(request, item_id):
    """ 
    Remove a product from the shopping bag
    
    """
    try:
        product = get_object_or_404(Product, pk=item_id)  
        shopping_bag = request.session.get('shopping_bag', {})

        # print(f"Current shopping bag contents: {shopping_bag}")
        
        if str(item_id) in shopping_bag:
            shopping_bag.pop(str(item_id))
            messages.success(request, f'Removed {product.name} from your bag')
            
        else: 
            messages.warning(request, f' Sorry Item not found')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)
    except Exception as e:
        print(f"Error removing item: {e}")
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


