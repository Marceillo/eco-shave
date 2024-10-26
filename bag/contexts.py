from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    """
    This provides an update of the shopping contents.
    """
    shopping_bag = request.session.get('shopping_bag', {})
    items_in_bag_contents = sum(shopping_bag.values())
    product_dict = {}

    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_dict[item_id] = {
            'product': product,
            'quantity': quantity,
        }

    context = {
        'items_in_bag_contents': items_in_bag_contents,
        'product_dict': product_dict,
    }
    return context


