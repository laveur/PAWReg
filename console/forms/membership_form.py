from django import forms

from shared.models import Event, ProductType, Product, Membership

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = (
            'name_short',
            'name_long',
            'product_description',
            'tier1_pricing',
            'tier2_pricing',
            'tier3_pricing',
            'available_at_event',
            'available_pre_event',
            'included_products',
        )
