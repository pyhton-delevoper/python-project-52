from django.urls import path
from task_manager.login import views


urlpatterns = [
    path('', views.UserLogin.as_view(), name='login')
]