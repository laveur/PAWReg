from django.views.generic.base import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from merchant.forms import TableForm

class TableCreatePageView(TemplateView):
    template_name = 'table_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = TableForm()

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = TableForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('merchant:table-list'))

        return self.render_to_response(context)
