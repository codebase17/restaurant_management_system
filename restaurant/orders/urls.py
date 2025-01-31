from django.urls import path
from .views import product_list, create_order, order_success

urlpatterns = [
    path('', product_list, name='product_list'),
    path('order/', create_order, name='create_order'),
    path('order/success/', order_success, name='order_success'),
]