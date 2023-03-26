from django import forms

from shared.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('is_parent', 'is_merchant', 'is_party_host', 'is_volunteer')