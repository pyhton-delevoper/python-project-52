from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from task_manager.statuses.models import Status


statuses = Status.objects.all()
executors = User.objects.all()


class Task(models.Model):
    name = models.CharField(
        max_length=150
    )
    description = models.TextField(
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author'
    )
    # status = models.ForeignKey(
    #     Status,
    #     on_delete=models.PROTECT,
    #     blank=True,
    #     choices=statuses,
    #     related_name='status_set'
    # )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        choices=executors
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_at', 'author']
