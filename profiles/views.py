from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import  Order
from products.models import Product

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
  

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')  

    else:
        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'email': request.user.email,
        
    }

    return render(request, template, context)

# def edit_profile(request):
#     """
#     For the user to update there details in profile. 
#     """
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profiles')


#     else:
#         form = UserProfileForm(instance=request.user)
#         return render(request, 'profiles/edit_profile.html', {'form': form})



def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    
    return render(request, template, context)

@login_required
def wishlist(request):
    """
    This is the view for the wishlist.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    products = profile.wish_list.all()

    template = 'profiles/wish_list.html'
    context = {
        'wishlist': products,
    }
    return render(request, template, context)



@login_required
def add_to_wishlist(request, product_id):
    """
    To add a product to the wish list.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, id=product_id)

    if profile.wish_list.filter(id=product.id).exists():
        profile.wish_list.remove(product)
        messages.success(request, f'Removed {product.name} from your wishlist.')
        return redirect('wishlist')
    else:
        profile.wish_list.add(product)
        messages.success(request, f'Added {product.name} to your wishlist.')

    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    """
    To remove a wish list item.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, id=product_id) 
   
    if request.method == 'POST':
        if profile.wish_list.filter(id=product.id).exists():
            profile.wish_list.remove(product)
            messages.success(request, f'Removed {product.name} from your wishlist.')
        else:
            messages.info(request, f'{product.name} is not in your wishlist.')

    return redirect('wishlist')



