from django.conf import settings
from django.db import models

from shared.models import Event, Membership

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, blank=True, null=True)
    is_parent = models.BooleanField(verbose_name="I am bringing child", default=False)
    is_merchant = models.BooleanField(verbose_name="I am planning to be a Merchant", default=False)
    is_party_host = models.BooleanField(verbose_name="I am planning to host a party", default=False)
    is_volunteer = models.BooleanField(verbose_name="I want to volunteer", default=False)
    is_paid = models.BooleanField(verbose_name="Registration is paid", default=False)
