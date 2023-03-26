from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from shared.models import get_current_event
from shared.models import Event, User, Membership, Registration, RegistrationProduct, Product, ProductTypeAttribute


@method_decorator(login_required, name='dispatch')
class RegisterPartyPageView(TemplateView):
    template_name = 'register_party.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
