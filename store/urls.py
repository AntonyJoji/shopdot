from django.urls import path
from .views import *
urlpatterns = [
    path('',landing_page),
    path('storehome/',store_home),
    path('productpage/',product_page),
    path('details/<str:key>/',product_details),
    path('addtocart/',addtocart),
    path('cart/',shopping_cart),

]