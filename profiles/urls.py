from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    # path('', views.edit_profile, views.edit_profile, name='edit_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]