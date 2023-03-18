from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class UserLogin(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login/login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if not user:
            messages.add_message(
                request, messages.ERROR, extra_tags='alert-danger',
                message=
                '''Пожалуйста, введите правильные имя пользователя и пароль. 
                Оба поля могут быть чувствительны к регистру.'''
            )
            return render(request, 'login/login.html', {'username': username})

        login(request, user)
        messages.add_message(
            request, messages.SUCCESS, extra_tags='alert-success',
            message='Вы залогинены'
        )
        return redirect('index')
    

def logout_view(request):
    logout(request)
    messages.add_message(
        request, messages.INFO, extra_tags='alert-info',
        message='Вы разлогинены'
    )
    return redirect('index')
