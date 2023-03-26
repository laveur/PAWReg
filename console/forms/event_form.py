from django import forms

from shared.models import Event, ProductType, Product, Membership


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
