from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from shared.models import get_current_event
from shared.models import Event, User, Registration, Membership
from merchant.models import Merchant

from merchant.forms import MerchantForm

@method_decorator(login_required, name='dispatch')
class RegisterMerchantPageView(TemplateView):
    template_name = 'register_merchant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = get_current_event()
        registration = Registration.objects.get(user=self.request.user, event=event)
        membership = registration.membership
        
        merchant = None
        try:
            merchant = Merchant.objects.get(event=event, user=self.request.user)
        except Merchant.DoesNotExist:
            merchant = None
        
        context['event'] = event
        context['registration'] = registration
        context['membership'] = membership
        context['merchant'] = merchant
        context['form'] = MerchantForm(instance=merchant)

        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = MerchantForm(request.POST, instance=context['merchant'])
        context['form'] = form

        if form.is_valid:
            merchant = form.save(commit=False)
            merchant.event = context['event']
            merchant.user = request.user
            merchant.save()
        else:
            return self.render_to_response(context)
        
        if context['registration'].is_party_host:
            return HttpResponseRedirect(reverse('client:register-party'))
        elif context['registration'].is_volunteer:
            return HttpResponseRedirect(reverse('client:register-volunteer'))
        else:
            return HttpResponseRedirect(reverse('client:register-payment'))
        endif
