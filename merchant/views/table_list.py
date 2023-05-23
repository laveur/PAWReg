from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from merchant.models import Table

class TableListPageView(TemplateView):
    template_name = 'table_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tables'] = Table.objects.all()

        return context