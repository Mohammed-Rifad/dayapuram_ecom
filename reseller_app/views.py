from django.shortcuts import render

# Create your views here.

def reseller_home(request):
    return render(request,'reseller_app/reseller_home.html')

def product_catalogue(request):
    return render(request,'reseller_app/catalogue.html')

def add_product(request):
    return render(request,'reseller_app/add_product.html')

def my_order(request):
    return render(request,'reseller_app/my_orders.html')

def update_stock(request):
    return render(request,'reseller_app/update_stock.html')

def recent_orders(request):
    return render(request,'reseller_app/recent_orders.html')

 
 


