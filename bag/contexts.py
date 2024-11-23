from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    product_dict = {}
    total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        product_dict[item_id] = {
            'quantity': quantity,
            'product': product,
        }

    context = {
        'product_dict': product_dict,
        'total': total,
        'product_count': product_count,
        'shopping_bag': shopping_bag,
    }
    return context
