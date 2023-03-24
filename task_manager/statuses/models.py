from django.db import models
from django.forms import ModelForm

class Status(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


class StatusCreateForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
