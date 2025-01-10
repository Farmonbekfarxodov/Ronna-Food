from django.shortcuts import render
from .models import BlogShopModel


def products_page_view(request):
    blog_shops = BlogShopModel.objects.all()
    context = {
        blog_shops : 'blog_shops'
    }
    return render(request,'shop/shop.html',context)


def product_detail_view(request,pk):
    blog_shop = BlogShopModel.objects.filter(id=pk).first()
    if blog_shop is not None:
        context = {
            "blog_shop":blog_shop
        }
        return render(request,'shop/single-shop.html',context)
    else:
        return render(request,'pages/404.html')

