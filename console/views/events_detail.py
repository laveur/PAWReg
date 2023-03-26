from django.views.generic.base import TemplateView

from shared.models import Event, Product, Membership

from ..forms import EventForm

class EventsDetailsPageView(TemplateView):
    template_name = 'events_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = Event.objects.get(pk=kwargs['event_id'])
        memberships = Membership.objects.filter(event=event)
        products = Product.objects.all().filter(event=event)

        context['memberships'] = memberships
        context['products'] = products
        context['event'] = event

        context['form'] = EventForm(instance=event)
        
        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = EventForm(request.POST, instance=context['event'])
        context['form'] = form
        
        if form.is_valid():
            form.save()

        return self.render_to_response(context)