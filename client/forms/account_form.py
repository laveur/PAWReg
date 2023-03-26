from django.contrib.auth.forms import UserChangeForm

from shared.models import User

class AccountForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
