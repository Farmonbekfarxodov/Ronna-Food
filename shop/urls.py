from django.urls import path
from .views import product_list_view,product_detail_view

app_name = 'shop'

urlpatterns = [
    path('<int:pk>/',product_detail_view,name='product_detail'),
    path('', product_list_view, name='products'),
  
]


