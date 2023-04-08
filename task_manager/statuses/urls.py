from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesList.as_view(), name='statuses_list'),
    path('create/', views.StatusCreate.as_view(), name='status_create'),
    path(
        '<int:pk>/update/', views.StatusUpdate.as_view(), name='status_update'
    ),
    path(
        '<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'
    )
]
