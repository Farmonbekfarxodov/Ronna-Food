from django.shortcuts import render

from shop.models import ProductCategoryModel,ProductModel


def product_list_view(request):
    categories = ProductCategoryModel.objects.all()
    products = ProductModel.objects.all()
    q = request.GET.get('q')
    if q:
        products = products.filter(title__icontains=q)
        
    context = {
        'products':products,
        'categories':categories,
        
    }
    return render(request,'shop/shop.html',context)

def product_detail_view(request,pk):
    try:
        product = ProductModel.objects.get(id=pk)
    except ProductModel.DoesNotExist:
        return render(request,'pages/404.html')
    related_products = ProductModel.objects.filter(categories__in=[cat.id for cat in product.categories.all()])
    context = {
        "product":product,
        "related_products" : related_products
    }

    return render(request,'shop/single-shop.html',context)
