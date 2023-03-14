from django.forms import ModelForm
from task_manager.users.models import Users

class LoginForm(ModelForm):

    class Meta:

        model = Users
        fields = [
            'username', 'password'
        ]
