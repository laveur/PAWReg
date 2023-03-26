from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..forms import MembershipForm
from shared.models import Event, Membership

class MembershipsCreatePageView(TemplateView):
    template_name = 'memberships_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        event = Event.objects.get(pk=kwargs['event_id'])
        context['event'] = event
        context['form'] = MembershipForm()

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        form = MembershipForm(request.POST)
        context['form'] = form

        if form.is_valid():
            membership = form.save(commit=False)
            membership.event = context['event']
            membership.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('console:events-detail', args=[context['event'].id]))
        
        return self.render_to_response(context)