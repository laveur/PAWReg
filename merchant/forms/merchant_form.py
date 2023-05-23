from django import forms

from merchant.models import Merchant


class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = (
            'table_size',
            'business_name',
            'wares_description',
            'helper_legal_name',
            'helper_fan_name',
            'special_requests',
        )