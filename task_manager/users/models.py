from django.contrib.auth.models import User as Generic
from django.contrib.auth.forms import UserCreationForm


class User(Generic):

    def __str__(self):
        return self.get_full_name()


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name',
            'username', 'password1', 'password2'
        ]
