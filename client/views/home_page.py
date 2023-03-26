from django.views.generic.base import TemplateView

from ..forms.signin_form import SigninForm

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_authenticated'] = True;
        else: 
            context['signin_form'] = SigninForm()
        return context
