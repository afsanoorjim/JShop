from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order
from import_export import resources

class ProductResource(resources.ModelResource):
    
    class Meta:
        model = Product

admin.site.register(Category)
admin.site.register(Product, ProductResource)
admin.site.register(Order)