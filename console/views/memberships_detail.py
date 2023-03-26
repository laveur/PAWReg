from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..forms import MembershipForm
from shared.models import Event, Membership


class MembershipsDetailPageView(TemplateView):
    template_name = 'memberships_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = Event.objects.get(pk=kwargs['event_id'])
        membership = Membership.objects.get(pk=kwargs['membership_id'])

        context['event'] = event
        context['membership'] = membership

        context['form'] = MembershipForm(instance=membership)

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = MembershipForm(request.POST, instance=context['membership'])
        context['form'] = form

        if form.is_valid():
            form.save()

        return self.render_to_response(context)