from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('storehome/', store_home, name='store_home'),
    path('productpage/', product_page, name='product_page'),
    path('details/<str:key>/', product_details, name='product_details'),
    path('addtocart/', addtocart, name='addtocart'),
    path('cart/', shopping_cart, name='shopping_cart'),  
    path('deletecart/<str:key>/', delete_cart_item, name='delete_cart_item'), 
]
