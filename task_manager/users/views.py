from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


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
        User.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            password=request.POST['password1'],
        ).save()
        messages.add_message(
            request, messages.SUCCESS, extra_tags='alert-success',
            message='Пользователь успешно зарегистрирован'
        )
        return redirect('login')


class UserUpdate(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])

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
        user.set_password(request.POST['password1'])
        user.save()
        messages.add_message(
            request, messages.SUCCESS, extra_tags='alert-success',
            message='Пользователь успешно изменён'
        )
        return redirect('users_list')
    
    def handle_no_permission(self):
        messages.error(
            self.request,
            'Вы не авторизованы! Пожалуйста, выполните вход.',
            'alert-danger'
        )
        return super().handle_no_permission()


class UserDelete(View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=kwargs['id'])

        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR, extra_tags='alert-danger',
                message='Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect('login')

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
