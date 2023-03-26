from django.db import models

from shared.models import Membership,Product

class RegistrationProduct(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.TextField(default="", verbose_name="Attribute Value")
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Value")