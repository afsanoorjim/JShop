from django.urls import path
from .views import product_list, landing_page, order_list

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('shop/', product_list, name='product_list'),
    path('orders/', order_list, name='order_list'),
    path('category/<slug:category_slug>/', product_list, name='product_list_by_category'),
]
