from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from task_manager.users.forms import RegistrationForm


class ShowUsers(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(
            request, 'users/all_users.html', {'users': users}
        )


class UserCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/create.html')
    
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data)
            messages.add_message(
                request, messages.SUCCESS, extra_tags='alert-success',
                message='Пользователь успешно зарегистрирован'
            )
            return redirect('login')
        return render(
            request, 'users/create.html', {'form': form}
        )
    

class UserUpdate(View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])

        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR, extra_tags='alert-danger',
                message='Вы не авторизованы! Пожалуйста, выполните вход.'
            )

        if request.user.username != user.username:
            messages.add_message(
                request, messages.ERROR, extra_tags='alert-danger',
                message='У вас нет прав для изменения этого пользователя.'
            )
            return redirect('users_list')

        return render(request, 'users/update.html', {'user': user})
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['id'])
        user.username = request.POST['username']
        user.set_password(request.POST['password'])
        user.save()
        messages.add_message(
            request, messages.SUCCESS, extra_tags='alert-success',
            message='Пользователь успешно изменён'
        )
        return redirect('users_list')
        return render(
            request, 'users/update.html', {'form': form}
        )
    

class UserDelete(View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])

        if request.user.username != user.username:
            messages.add_message(
                request, messages.ERROR, extra_tags='alert-danger',
                message='У вас нет прав для изменения этого пользователя.'
            )
            return redirect('users_list')

        return render(
            request, 'users/delete.html', {'user': user}
        )
    
    def post(self, request, *args, **kwargs):
        User.objects.get(id=kwargs[id]).delete()
        messages.add_message(
            request, messages.SUCCESS, extra_tags='alert-success',
            message='Пользователь успешно удалён'
        )
        return redirect('users_list')
