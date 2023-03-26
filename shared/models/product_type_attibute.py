from django.db import models

from .product_type import ProductType

class ProductTypeAttribute(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name_short = models.CharField(max_length=50, verbose_name="Short Name")
    name_long = models.CharField(max_length=150, verbose_name="Long Name")

    def __str__(self):
        return self.name_long
