from django.contrib import admin
from .models import ProductCategoryModel, ProductImageModel, ProductModel

# Admin for ProductCategoryModel
@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

# Inline admin for ProductImageModel
class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel

# Admin for ProductModel
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    inlines = [ProductImageModelAdmin]  # Reference the inline class here
