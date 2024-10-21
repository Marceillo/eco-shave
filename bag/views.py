from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages # messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


# def add_to_bag( request, item_id):
#     """
#     Add products to the shopping bag. 
#     """








