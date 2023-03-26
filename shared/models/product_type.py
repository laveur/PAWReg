from django.db import models

class ProductType(models.Model):
    name_short = models.CharField(max_length=50, verbose_name="Short Name")
    name_long = models.CharField(max_length=150, verbose_name="Long Name")
    user_selection_required = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name_long
