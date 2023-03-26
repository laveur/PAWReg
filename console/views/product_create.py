from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..forms import ProductForm
from shared.models import Event, Membership, Product

class ProductCreatePageView(TemplateView):
    template_name = 'products_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = Event.objects.get(pk=kwargs['event_id'])
        context['event'] = event
        context['form'] = ProductForm()

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        event = Event.objects.get(pk=kwargs['event_id'])
        
        form = ProductForm(request.POST)
        context['form'] = form

        if form.is_valid():
            product = form.save(commit=False)
            product.event = event
            product.save()
            return HttpResponseRedirect(reverse('console:events-detail', args=[event.id]))
        
        return self.render_to_response(context)