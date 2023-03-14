from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from task_manager.login.forms import LoginForm
from task_manager.users.models import Users

# Create your views here.
class UserLogin(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(
            request, 'login/login.html', {'form': form}
        )
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('passsword')
        users = Users.objects.all()
        try:
            users.get(username=username, password=password)
        except Users.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, extra_tags='alert-danger',
                message=
                '''Пожалуйста, введите правильные имя пользователя и пароль. 
                Оба поля могут быть чувствительны к регистру.'''
            )
            return render(
                request, 'login/login.html', {'form': form}
            )
        messages.add_message(
            request, messages.SUCCESS, extra_tags='alert-success',
            message='Вы залогинены'
        )
        return redirect('index')

