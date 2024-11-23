from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path(
        'contact/contact_success/',
        views.contact_success,
        name='contact_success',
    ),
    path('faqs/', views.faq, name='faq'),
    path('faqs/add/', views.add_faq, name='add_faq'),
    path('faqs/edit/<int:pk>/', views.edit_faq, name='edit_faq'),
    path('faqs/delete/<int:pk>/', views.delete_faq, name='delete_faq'),
]
