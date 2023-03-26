from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    address_line1 = models.CharField(max_length=100, verbose_name="Address")
    address_line2 = models.CharField(max_length=100, blank=True, verbose_name="Address Line 2")
    address_city = models.CharField(max_length=100, verbose_name="City")
    address_province = models.CharField(max_length=100, verbose_name="State/Province")
    address_country = models.CharField(max_length=100, verbose_name="Country")
    address_postal_code = models.CharField(max_length=15, verbose_name="Postal Code")
    phone_number = models.CharField(max_length=50, verbose_name="Phone Number")
    emergency_contact_name = models.CharField(max_length=100, verbose_name="Emergency Contact")
    emergency_contact_phone = models.CharField(max_length=50, verbose_name="Emergency Contact Phone")
    birthdate = models.DateField()
    badge_name = models.CharField(max_length=50, verbose_name="Badge Name")
