from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..forms import RegistrationForm
from shared.models import get_current_event
from shared.models import Event, Membership, User, Registration


@method_decorator(login_required, name='dispatch')
class RegisterPageView(TemplateView):
    template_name = 'home_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = get_current_event()
        registration = None
        try:
            registration = Registration.objects.get(user=self.request.user, event=event)
        except Registration.DoesNotExist:
            registration = None
    
        context['registration'] = registration
        
        context['form'] = RegistrationForm(instance=registration)

        return context
    
    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        form = RegistrationForm(request.POST, context['registration'])
        context['form'] = form

        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = get_current_event()
            registration.user = request.user
            registration.save()
            return HttpResponseRedirect(reverse('client:register-membership'))
        
        return self.render_to_response(context)