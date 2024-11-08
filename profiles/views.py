from django.shortcuts import render, redirect, get_object_or_404
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
    # wish_list = current_user.wish_list.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
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
        # 'wish_list': wish_list,
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
    For display of user wish list 
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wish_list = profile.wish_list.all()

    context = {
        'wish_list': wish_list,
        'wish_list_page': True,
    }
    
    return render(request, 'profiles/wish_list.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    To add to the wish list 
    """
    product = get_object_or_404(Product, id=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    try:
        if product not in profile.wish_list.all():
            profile.wish_list.add(product)
            messages.success(request, f'{product.name} has been added to your wish list.')
        else:
            messages.info(request, f'{product.name} is already in your wish list.')

    except Exception as e:
        messages.error(request, f'There was a problem adding {product.name} to your wish list: {str(e)}')
        
        return redirect('wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    """
    To add to the wish list 
    """
    product = get_object_or_404(Product, id=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    try:
        if product not in profile.wish_list.all():
            profile.wish_list.remove(product)
            messages.success(request, f'{product.name} has been removed from your wish list.')
        else:
            messages.info(request, f'{product.name} is  not in your wish list.')

    except Exception as e:
        messages.error(request, f'There was a error removing {product.name} from your wish list: {str(e)}')
        
        return redirect('wishlist')



