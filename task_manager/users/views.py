from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.db.models import ProtectedError
from django.contrib import messages
from .models import UserCreateForm
from task_manager.views import MyLoginRequiredMixin


class UsersList(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(
            request, 'users/list.html', {'users': users}
        )


class UserCreate(View):

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(
            request, 'users/create.html', {'form': form}
        )
    
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.data['password'])
            user.save()
            messages.success(
                request,
                'Пользователь успешно зарегистрирован',
                'alert-success'
            )
            return redirect('login')
        return render(
            request, 'users/create.html', {'form': form}
        )


class UserUpdate(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])

        if request.user.username != user.username:
            messages.error(
                request,
                'У вас нет прав для изменения этого пользователя.',
                'alert-danger'
            )
            return redirect('users_list')
        
        form = UserCreateForm(instance=user)
        return render(
            request, 'users/update.html', {'form': form, 'id': user.id}
        )
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        form = UserCreateForm(request.POST, instance=user)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.data['password1'])
            user.save()
            messages.success(
                request,
                'Пользователь успешно изменён',
                'alert-success'
            )
            return redirect('users_list')

        return render(
            request, 'users/update.html', {'form': form}
        )


class UserDelete(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            user = get_object_or_404(User, id=kwargs['pk'])
        except ProtectedError:
            messages.error(
                request,
                '''Невозможно удалить пользователя, 
                   потому что он используется''',
                'alert-danger'
            )

        if request.user.username != user.username:
            messages.error(
                request,
                'У вас нет прав для изменения этого пользователя.',
                'alert-danger'
            )
            return redirect('users_list')

        return render(
            request, 'users/delete.html', {'user': user}
        )
    
    def post(self, request, *args, **kwargs):
        User.objects.get(id=kwargs['pk']).delete()
        messages.success(
            request,
            'Пользователь успешно удалён',
            'alert-success'
        )
        return redirect('users_list')
