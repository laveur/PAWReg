from django.db import models

class Table(models.Model):
    key = models.CharField(max_length=4, primary_key=True, verbose_name="Internal Key")
    name = models.CharField(max_length=20, verbose_name="Table Name")
    order = models.IntegerField(default=0, verbose_name="Order to display")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Table Cost")

    def __str__(self):
        return self.name
