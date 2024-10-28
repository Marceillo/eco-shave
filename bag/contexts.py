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
    


#  view_bag(request):
#     """ 
#     This is for the bag contents.
#     """          
#     shopping_bag = request.session.get('shopping_bag', {})
#     total_items = sum(shopping_bag.values())
#     products = Product.objects.filter(pk__in=shopping_bag.keys())
    
    
#     total_price = sum(product.price * shopping_bag[str(product.pk)] for product in products)

#     product_dict = {
#         str(product.pk): {
#             'product': product,
#             'quantity': shopping_bag[str(product.pk)]
#         } for product in products
#     }

#     context = {
#         'shopping_bag': shopping_bag,
#         'total_items': total_items,
#         'total_price': total_price,
#         'product_dict': product_dict,
#     }

#     return render(request, 'bag/bag.html', context) 
# from django.conf import settings
# from django.shortcuts import get_object_or_404
# from products.models import Product

   
# from decimal import Decimal
# from django.shortcuts import get_object_or_404
# from products.models import Product

# def bag_contents(request):
#     shopping_bag = request.session.get('shopping_bag', {})
#     total_price = 0
#     total_items = 0
#     product_dict = {}

#     for item_id, quantity in shopping_bag.items():
#         product = get_object_or_404(Product, pk=item_id)
#         total_price += quantity * product.price
#         total_items += quantity
#         product_dict[str(item_id)] = {
#             'product': product,
#             'quantity': quantity,
#         }

#     return {
#         'shopping_bag': shopping_bag,
#         'total_items': total_items,
#         'total_price': total_price,
#         'product_dict': product_dict,
#     }