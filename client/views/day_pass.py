from django.views.generic.base import TemplateView

class DayPassPageView(TemplateView):
    template_name = 'home_day_pass.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context