from django.views.generic.base import TemplateView

class ForgotPasswordPageView(TemplateView):
    template_name = 'home_forgot_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context