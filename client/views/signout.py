from django.contrib.auth import logout
from django.views.generic.base import RedirectView

class SignoutPageView(RedirectView):
    pattern_name = 'client:index'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
