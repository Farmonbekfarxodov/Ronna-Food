from django.urls import path
from .views import products_page_view, product_detail_view

app_name = 'shop'

urlpatterns = [
    path('', products_page_view, name='products'),
    path('<int:pk>/', product_detail_view, name='single_product'),
]


