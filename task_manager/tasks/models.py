from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
import django_filters


statuses = Status.objects.all()
executors = User.objects.all()
labels = User.objects.all()


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        blank=True,
        choices=statuses,
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        choices=executors,
        related_name='executor'
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        choices=labels
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_at', 'author']


class TaskFilterForm(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
