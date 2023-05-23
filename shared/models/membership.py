from django.db import models

from .event import Event
from .product import Product

class Membership(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name_short = models.CharField(max_length=50, verbose_name="Short Name")
    name_long = models.CharField(max_length=150, verbose_name="Long Name")
    product_description = models.TextField(max_length=200, verbose_name="Product Description")
    tier1_pricing = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Tier 1 Pricing")
    tier2_pricing = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Tier 2 Priciing")
    tier3_pricing = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Tier 3 Pricing")
    available_at_event = models.BooleanField(default=True, verbose_name="At Event Availability")
    available_pre_event = models.BooleanField(default=True, verbose_name="Pre Event Availability")
    available_parents = models.BooleanField(default=False, verbose_name="Available to Parents")
    available_merchants = models.BooleanField(default=False, verbose_name="Available to Merchants")
    included_products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name_long
