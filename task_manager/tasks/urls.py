from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksList.as_view(), name='tasks_list'),
    path('create/', views.TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/', views.TaskView.as_view(), name='task_view'),
    path('<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete')
]
