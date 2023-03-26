from django.urls import reverse
from django.views.generic.base import TemplateView

from ..forms import ProductForm
from shared.models import Event, Product

class ProductDetailPageView(TemplateView):
    template_name = 'products_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = Event.objects.get(pk=kwargs['event_id'])
        product = Product.objects.get(pk=kwargs['product_id'])

        context['event'] = event
        context['product'] = product
        context['form'] = ProductForm(instance=product)

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = ProductForm(request.POST, instance=context['product'])
        context['form'] = form
        
        if form.is_valid():
            form.save()

        return self.render_to_response(context)