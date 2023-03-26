from django.db import models


class Event(models.Model):
    name_short = models.CharField(max_length=50, verbose_name="Short Name")
    name_long = models.CharField(max_length=150, verbose_name="Long Name")
    event_start_date = models.DateField(verbose_name="Event Start")
    event_end_date = models.DateField(verbose_name="Event End")
    event_tier1_pricing_start = models.DateField(
        verbose_name="Tier 1 Pricing Start")
    event_tier2_pricing_start = models.DateField(
        verbose_name="Tier 2 Pricing Start")
    event_tier3_pricing_start = models.DateField(
        verbose_name="Tier 3 Pricing Start")
    partyfloor_rooms_available = models.IntegerField(
        default=0, verbose_name="Part Floor Available")
    merchants_spots_available = models.IntegerField(
        default=0, verbose_name="Merchant Spots Available")

    def __str__(self):
        return self.name_short
