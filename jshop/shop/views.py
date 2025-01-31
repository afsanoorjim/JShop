from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Order

def landing_page(request):
    return render(request, 'shop/landing_page.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product_list.html', {'products': products, 'category': category, 'categories': categories})

def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'shop/order_list.html', {'orders': orders})