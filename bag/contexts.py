from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    product_dict = []
    total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})
      
    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        product_dict.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'product_dict': product_dict,
        'total': total,
        'product_count': product_count,
    }
    return context

# my first

# def bag_contents(request):
#     """
#     This provides an update of the shopping contents.
#     """
#     shopping_bag = request.session.get('shopping_bag', {})
#     items_in_bag_contents = sum(shopping_bag.values())
#     product_dict = {}

#     for item_id, quantity in shopping_bag.items():
#         product = get_object_or_404(Product, pk=item_id)
#         product_dict[item_id] = {
#             'product': product,
#             'quantity': quantity,
#         }

#     context = {
#         'items_in_bag_contents': items_in_bag_contents,
#         'product_dict': product_dict,
#     }
#     return context




    # another exmaple 

# def bag_contents(request):
#     items_details = []
#     total = 0
#     product_count = 0
#     shopping_bag = request.session.get('shopping_bag', {})

    
#     for item_id, quantity in shopping_bag.items():
#         product = get_object_or_404(Product, pk=item_id)
#         total += quantity * product.price
#         product_count += quantity
#         items_details.append({
#             'item_id': item_id,
#             'product_count': product_count,
#             'product': product,
#         })

#     context = {
#         'items_details': items_details,
#         'total': total,
#         'product_count': product_count,
#     }
#     return context