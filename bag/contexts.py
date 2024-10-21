from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def shopping_bag(request):
    """
    
    """
    
    shopping_bag = request.session.get('bag', {})
    context = {'items_in_bag': sum(shopping_bag.values())}
    return context


