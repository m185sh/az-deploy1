from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/',views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),  # Create this view or template for success message
    
]
