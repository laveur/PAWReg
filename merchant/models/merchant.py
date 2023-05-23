from django.conf import settings
from django.db import models

from merchant.models import Table
from shared.models import Event

class Merchant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table_size = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    business_name = models.CharField(max_length=200)
    wares_description = models.TextField('Description of Wares')
    helper_legal_name = models.CharField(max_length=200, blank=True)
    helper_fan_name = models.CharField(max_length=200, blank=True)
    special_requests = models.TextField(blank=True)
    table_number = models.IntegerField(null=True, blank=True)
    table_assigned = models.BooleanField(default=False)

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.business_name)
