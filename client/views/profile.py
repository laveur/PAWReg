from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from ..forms import AccountForm, ProfileForm
from shared.models import Profile


@method_decorator(login_required, name='dispatch')
class ProfilePageView(TemplateView):
    template_name = 'home_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = None
        if Profile.objects.filter(user=self.request.user).count() > 0:
            profile = Profile.objects.get(user=self.request.user)

        account_form = AccountForm(instance=self.request.user)
        profile_form = ProfileForm(instance=profile)

        context['account_form'] = account_form
        context['profile_form'] = profile_form

        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form_name = request.POST['form']

        if form_name == 'Account':
            account_form = AccountForm(request.POST, instance=self.request.user)

            context['account_form'] = account_form

            if account_form.is_valid():
                account_form.save()

        if form_name == 'Profile':
            profile = None
            if Profile.objects.filter(user=self.request.user).count() > 0:
                profile = Profile.objects.get(user=self.request.user)

            profile_form = ProfileForm(self.request.POST, instance=profile)

            context['profile_form'] = profile_form

            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = self.request.user
                profile.save()
        
        return self.render_to_response(context)
        

