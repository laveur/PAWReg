from django import forms

from merchant.models import Table

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = (
            'key',
            'name',
            'order',
            'price'
        )

