from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history',
    ),
    path('wishlist/', views.wishlist, name='wishlist'),
    path(
        'wishlist/add/<int:product_id>/',
        views.add_to_wishlist,
        name='add_to_wishlist',
    ),
    path(
        'wishlist/remove/<int:product_id>/',
        views.remove_from_wishlist,
        name='remove_from_wishlist',
    ),
]
