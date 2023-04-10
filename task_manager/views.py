from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def index(request, *args, **kwargs):
    return render(request, 'index.html')


class UserLoginView(LoginView):
    template_name = 'login/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        messages.success(
            self.request,
            'Вы залогинены',
            'alert-success'
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request):
        messages.success(
            request, 'Вы разлогинены', 'alert-info'
        )
        return super().dispatch(request)


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                'Вы не авторизованы! Пожалуйста, выполните вход.',
                'alert-danger'
            )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
