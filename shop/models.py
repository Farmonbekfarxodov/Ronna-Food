from django.db import models
from recipe.models import BaseModel


class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    

class ProductModel(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    is_stock = models.BooleanField(default=True)
    sku = models.CharField(max_length=7, unique=True)
    categories = models.ManyToManyField(ProductCategoryModel,related_name='products')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
    

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, 
                                related_name='images')
    image = models.ImageField(upload_to="products")
