from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django.forms import CheckboxInput
from .models import Task
from task_manager.labels.models import Label


class TaskFilterForm(FilterSet):
    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка'
    )
    own_tasks = BooleanFilter(
        method='filter_own',
        widget = CheckboxInput,
        label='Только свои задачи'
    )

    def filter_own(self, qs, name, value):   
        if value:
            user = self.request.user
            return qs.filter(author=user)
        return qs

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
    