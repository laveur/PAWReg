from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView

from ..forms import SigninForm

class SigninPageView(TemplateView):
    template_name = 'home_signin.html'
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signin_form'] = SigninForm()
        return context
        
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        form = SigninForm(request.POST)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
