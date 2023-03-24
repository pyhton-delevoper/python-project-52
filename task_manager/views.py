from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def index(request, *args, **kwargs):
    return render(request, 'index.html')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request):
        messages.success(
            request, 'Вы разлогинены', 'alert-info'
        )
        return super().dispatch(request)
    

class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')
    
    def handle_no_permission(self):
        messages.error(
            self.request,
            'Вы не авторизованы! Пожалуйста, выполните вход.',
            'alert-danger'
        )
        return super().handle_no_permission()
