from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Event, ProductType, ProductTypeAttribute, Product, Membership, Registration, RegistrationProduct

# Register your models here.
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name_short', 'name_long', 'event_start_date', 'event_end_date')

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name_short', 'name_long')

@admin.register(ProductTypeAttribute)
class ProductTypeAttributeAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'name_short', 'name_long')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_short', 'name_long', 'product_description', 'tier1_pricing', 'tier2_pricing', 'tier3_pricing')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('name_short', 'name_long', 'product_description', 'tier1_pricing', 'tier2_pricing', 'tier3_pricing')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'membership')

@admin.register(RegistrationProduct)
class RegistrationProductAdmin(admin.ModelAdmin):
    list_displa  = ('membership', 'product', 'attribute', 'value')
