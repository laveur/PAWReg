from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from shared.models import get_current_event
from shared.models import Event, User, Membership, Registration, RegistrationProduct, Product, ProductTypeAttribute


@method_decorator(login_required, name='dispatch')
class RegisterPaymentPageView(TemplateView):
    template_name = 'register_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = get_current_event()
        registration = Registration.objects.get(user=self.request.user, event=event)
        context['registration'] = registration

        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        if request.POST.get('is_paid', False):
            context['registration'].is_paid = True
            context['registration'].save()
            return HttpResponseRedirect(reverse('client:index'))
        else:
            return self.render_to_response(context)
        endif