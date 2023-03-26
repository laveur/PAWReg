from django.db import models

from .event import Event
from .product_type import ProductType

class Product(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    product_type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, verbose_name="Product Type")
    name_short = models.CharField(max_length=50, verbose_name="Short Name")
    name_long = models.CharField(max_length=150, verbose_name="Long Name")
    product_description = models.TextField(
        max_length=200, verbose_name="Product Description")
    cart_max = models.IntegerField(
        verbose_name="Cart Max", help_text="Max allowed in a cart")
    tier1_pricing = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Tier 1 Pricing")
    tier2_pricing = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Tier 2 Priciing")
    tier3_pricing = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Tier 3 Pricing")
    customer_modifiable = models.BooleanField(
        default=False, verbose_name="Customer Modifiable")
    available_at_event = models.BooleanField(
        default=False, verbose_name="At Event Availability")
    available_pre_event = models.BooleanField(
        default=False, verbose_name="Pre Event Availability")

    def __str__(self):
        return self.name_long
