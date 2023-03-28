from django.shortcuts import render, redirect, get_object_or_404
from task_manager.views import MyLoginRequiredMixin
from django.views import View
from django.contrib import messages
from .models import Task, TaskCreateForm


class TasksList(MyLoginRequiredMixin, View):

    def get(self, request, **kwargs):
        tasks = Task.objects.all()
        return render(
            request, 'tasks/list.html', {'tasks': tasks}
        )


class TaskCreate(MyLoginRequiredMixin, View):

    def get(self, request, **kwargs):
        form = TaskCreateForm()
        return render(
            request, 'tasks/create.html', {'form': form}
        )

    def post(self, request, **kwargs):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Задача успешно создана',
                'alert-success'
            )
            return redirect('statuses_list')
        return render(
            request, 'tasks/create.html', {'form': form}
        )
    

class TaskView(MyLoginRequiredMixin, View):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        return render(
            request, 'tasks/view.html', {'task': task}
        )
        

class TaskUpdate(MyLoginRequiredMixin, View):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        form = TaskCreateForm(instance=task)
        return render(
            request, 'tasks/create.html',
            {'form': form, 'id': task.id}
        )

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Задача успешно изменена',
                'alert-success'
            )
            return redirect('statuses_list')
        return render(
            request, 'tasks/create.html',
            {'form': form, 'id': task.id}
        )


class TaskDelete(MyLoginRequiredMixin, View):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        if request.user.username != task.author:
            messages.error(
                request,
                'Задачу может удалить только её автор',
                'alert-danger'
            )
            return redirect('users_list')
        return render(
            request, 'tasks/delete.html', {'task': task}
        )
    
    def post(self, request, **kwargs):
        get_object_or_404(Task, id=kwargs['pk']).delete()
        messages.success(
                request,
                'Задача успешно удалена',
                'alert-success'
            )
        return redirect('tasks_list')
