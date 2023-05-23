from merchant.forms import TableForm
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from merchant.models import Table
from merchant.forms import TableForm

class TableDetailPageView(TemplateView):
    template_name = 'table_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        table = Table.objects.get(key=kwargs['key'])
        context['table'] = table
        context['form'] = TableForm(instance=table)

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = TableForm(request.POST, instance=context['table'])
        context['form'] = form

        if form.is_valid():
            form.save()
        
        return self.render_to_response(context)