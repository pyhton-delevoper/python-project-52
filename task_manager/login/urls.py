from django.urls import path
from task_manager.login import views


urlpatterns = [
    path('', views.UserLoginView.as_view(), name='login')
]
