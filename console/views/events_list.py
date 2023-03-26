from django.views.generic.base import TemplateView

from shared.models import Event

class EventsListPageView(TemplateView):
    template_name = 'events_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context