from django.contrib import admin

from merchant.models import Table, Merchant

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'price')

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'business_name')