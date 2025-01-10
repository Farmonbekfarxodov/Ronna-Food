from django.db import models

from recipe.models import BaseModel


class BlogShopModel(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'BlogShop'
        verbose_name_plural = 'BlogShops'

    def __str__(self):
        return self.name