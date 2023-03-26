from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class SigninForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(AuthenticationForm, *args, **kwargs)
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)
