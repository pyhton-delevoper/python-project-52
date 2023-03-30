from django.db import models
from django.forms import ModelForm
from task_manager.tasks.models import Task


class Label(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


class LabelCreateForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
