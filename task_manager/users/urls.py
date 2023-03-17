from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.ShowUsers.as_view(), name='users_list'),
    path('create/', views.UserCreate.as_view(), name='user_create'),
    path('<int:id>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('<int:id>/delete/', views.UserDelete.as_view(), name='user_delete'),
]
