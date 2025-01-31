from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Product, Category, Order

class ProductAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('customer__username', 'product__name')
    actions = ['mark_as_shipped', 'mark_as_delivered']

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='Shipped')

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='Delivered')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
