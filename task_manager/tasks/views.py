from django.shortcuts import render, redirect, get_object_or_404
from task_manager.views import MyLoginRequiredMixin
from django.views import View
from django_filters.views import FilterView
from django.contrib import messages
from .models import Task, TaskCreateForm
from .filters import TaskFilterForm


class TasksList(MyLoginRequiredMixin, FilterView):
    template_name = 'tasks/list.html'
    filterset_class = TaskFilterForm
    model = Task
    context_object_name = 'tasks'


class TaskCreate(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = TaskCreateForm()
        return render(
            request, 'tasks/create.html', {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            task.labels.add(request.POST.get('labels'))
            messages.success(
                request,
                'Задача успешно создана',
                'alert-success'
            )
            return redirect('tasks_list')
        return render(
            request, 'tasks/create.html', {'form': form}
        )
    

class TaskView(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        return render(
            request, 'tasks/view.html', {'task': task}
        )
        

class TaskUpdate(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        form = TaskCreateForm(instance=task)
        return render(
            request, 'tasks/update.html',
            {'form': form, 'id': task.id}
        )

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Задача успешно изменена',
                'alert-success'
            )
            return redirect('tasks_list')
        return render(
            request, 'tasks/create.html',
            {'form': form, 'id': task.id}
        )


class TaskDelete(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        if request.user.username != task.author.username:
            messages.error(
                request,
                'Задачу может удалить только её автор',
                'alert-danger'
            )
            return redirect('tasks_list')
        return render(
            request, 'tasks/delete.html', {'task': task}
        )
    
    def post(self, request, *args, **kwargs):
        get_object_or_404(Task, id=kwargs['pk']).delete()
        messages.success(
                request,
                'Задача успешно удалена',
                'alert-success'
            )
        return redirect('tasks_list')
