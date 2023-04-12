from django.db import models
from django.forms import ModelForm
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='author'
    )
    status = models.ForeignKey(
        Status,
        null=True,
        on_delete=models.PROTECT,
        blank=True,
        verbose_name='Статус'
    )
    executor = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        blank=True,
        related_name='executor',
        verbose_name='Исполнитель'
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        verbose_name='Метки'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_at', 'author']
