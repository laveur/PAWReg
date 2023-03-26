
from django import forms

from shared.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'address_line1',
            'address_line2',
            'address_city',
            'address_province',
            'address_country',
            'address_postal_code',
            'phone_number',
            'emergency_contact_name',
            'emergency_contact_phone',
            'birthdate',
            'badge_name'
        )
