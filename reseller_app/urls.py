from django.urls import path
from . import views

app_name = 'reseller'

urlpatterns = [
    path('',views.reseller_home, name='reseller_home'),
    path('p-catalogue',views.product_catalogue, name='catalogue'),
    path('update-stock',views.update_stock, name='update_stock'),
    path('product-add',views.add_product, name='add_product'),
    path('my-order',views.my_order, name='reseller_orders'),
    path('recent-orders',views.recent_orders, name='recent_orders')
    
]