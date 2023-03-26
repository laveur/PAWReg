from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..forms import EventForm

class EventsCreatePageView(TemplateView):
    template_name = 'events_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventForm()
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = EventForm(request.POST)
        context['form'] = form

        if form.is_valid:
            result = form.save()
            return HttpResponseRedirect(reverse('console:events-list'))
        
        return self.render_to_response(context)
