from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('contact/success/', views.contact_success, name='contact_success'),

]