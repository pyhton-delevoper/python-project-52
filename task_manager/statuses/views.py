from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Status, StatusCreateForm
from task_manager.views import MyLoginRequiredMixin


class StatusesList(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(
            request, 'statuses/list.html', {'statuses': statuses}
        )


class StatusCreate(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = StatusCreateForm()
        return render(
            request, 'statuses/create.html', {'form': form}
        )

    def post(self, request, *args, **kwargs):
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


class StatusUpdate(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, id=kwargs['pk'])
        form = StatusCreateForm(instance=status)
        return render(
            request, 'statuses/update.html',
            {'form': form, 'status': status}
        )

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, id=kwargs['pk'])
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
            request, 'statuses/update.html',
            {'form': form, 'status': status}
        )


class StatusDelete(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, id=kwargs['pk'])
        return render(
            request, 'statuses/delete.html', {'status': status}
        )

    def post(self, request, *args, **kwargs):
        try:
            get_object_or_404(Status, id=kwargs['pk']).delete()
        except ProtectedError:
            messages.error(
                request,
                '''Невозможно удалить статус,
                потому что он используется''',
                'alert-danger'
            )
            return redirect('statuses_list')
        messages.success(
            request,
            'Статус успешно удалён',
            'alert-success'
        )
        return redirect('statuses_list')
