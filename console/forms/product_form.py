from django import forms

from shared.models import Event, ProductType, Product, Membership

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_type',
            'name_short',
            'name_long',
            'product_description',
            'cart_max',
            'tier1_pricing',
            'tier2_pricing',
            'tier3_pricing',
            'customer_modifiable',
            'available_at_event',
            'available_pre_event',
        )
