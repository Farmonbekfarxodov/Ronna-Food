from django.contrib import admin

from .models import BlogShopModel

admin.site.register(BlogShopModel)
class BlogShopAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','is_active')
    list_filter =  ('is_active')
    search_fields = ('name','description')
    ordering = ('name',)
