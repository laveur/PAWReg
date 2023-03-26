from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from shared.models import get_current_event
from shared.models import Event, User, Membership, Registration


@method_decorator(login_required, name='dispatch')
class SelectMembershipPageView(TemplateView):
    template_name = 'register_membership.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = get_current_event()
        registration = Registration.objects.get(user=self.request.user, event=event)
        memberships = Membership.objects.filter(event=event)
        context['registration'] = registration
        context['memberships'] = memberships

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        membership = Membership.objects.get(pk=request.POST['membership'])
        context['registration'].membership = membership
        context['registration'].save()

        return HttpResponseRedirect(reverse('client:register-products'))