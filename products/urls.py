from django.urls import path, include
from . import views 


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    
    
    # path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    # path('upload-product/', upload_product_view, name='upload_product'),  
]