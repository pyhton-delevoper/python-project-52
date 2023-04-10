from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import ProtectedError
from django.contrib import messages
from task_manager.labels.models import Label, LabelCreateForm
from task_manager.views import MyLoginRequiredMixin


class LabelsList(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(
            request, 'labels/list.html', {'labels': labels}
        )


class LabelCreate(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = LabelCreateForm()
        return render(
            request, 'labels/create.html', {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = LabelCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Метка успешно создана',
                'alert-success'
            )
            return redirect('labels_list')
        return render(
            request, 'labels/create.html', {'form': form}
        )


class LabelUpdate(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        label = get_object_or_404(Label, id=kwargs['pk'])
        form = LabelCreateForm(instance=label)
        return render(
            request, 'labels/update.html',
            {'form': form, 'label': label}
        )

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Label, id=kwargs['pk'])
        form = LabelCreateForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Метка успешно изменена',
                'alert-success'
            )
            return redirect('labels_list')
        return render(
            request, 'labels/update.html',
            {'form': form, 'label': label}
        )


class LabelDelete(MyLoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        label = get_object_or_404(Label, id=kwargs['pk'])
        return render(
            request, 'labels/delete.html', {'label': label}
        )

    def post(self, request, *args, **kwargs):
        try:
            get_object_or_404(Label, kwargs['pk']).delete()
        except ProtectedError:
            messages.error(
                request,
                '''
                Невозможно удалить метку,   
                потому что она используется
                ''',
                'alert-danger'
            )
            return redirect('labels_list')
        messages.success(
            request,
            'Метка успешно удалена',
            'alert-success'
        )
        return redirect('labels_list')
