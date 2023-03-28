from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Status, StatusCreateForm
from task_manager.views import MyLoginRequiredMixin


class StatusesList(MyLoginRequiredMixin, View):

    def get(request, **kwargs):
        statuses = Status.objects.all()
        return render(
            request, 'statuses/list.html', {'statuses': statuses}
        )
    

class StatusCreate(MyLoginRequiredMixin, View):

    def get(self, request, **kwargs):
        form = StatusCreateForm()
        return render(
            request, 'statuses/create.html', {'form': form}
        )
    
    def post(self, request, **kwargs):
        form = StatusCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Статус успешно создан',
                'alert-success'
            )
            return redirect('statuses_list')
        return render(
            request, 'statuses/create.html', {'form': form}
        )


class StatusUpdate(StatusCreate):
    
    def get(self, request, **kwargs):
        status = Status.objects.get(id=kwargs['pk'])
        form = StatusCreateForm(instance=status)
        return render(
            request, 'statuses/create.html', {'form': form}
        )

    def post(self, request, **kwargs):
        status = Status.objects.get(kwargs['pk'])
        form = StatusCreateForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Статус успешно изменён',
                'alert-success'
            )
            return redirect('statuses_list')
        return render(
            request, 'statuses/create.html',
            {'form': form, 'id': status.id}
        )


class StatusDelete(MyLoginRequiredMixin, View):

    def get(self, request, **kwargs):
        return render(request, 'statuses/delete.html')

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, kwargs['pk'])
        #active_statuses = Task.objects.status_set
        status.delete()
        messages.success(
            request, 'Статус успешно удалёнэ', 'alert-success'
        )
        return redirect('statuses_list')
