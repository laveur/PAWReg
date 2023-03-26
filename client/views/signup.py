from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

from ..forms import SignupForm

class SignupPageView(TemplateView):
    template_name = 'home_signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_form'] = SignupForm()
        return context
    
    def post(self, request, **kwargs):
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid:
            signup_form.save()
            return HttpResponseRedirect('/')
        else:
            context = self.get_context_data(**kwargs)
            context['signup_form'] = signup_form
            return self.render_to_response(context)
