from django.views.generic.base import TemplateView

class ConsoleIndexPageView(TemplateView):
    template_name = 'console_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context