from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'login/login.html'

    def form_valid(self, form):
        messages.success(
            self.request,
            'Вы залогинены',
            'alert-success'
        )
        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            '''
            Введите правильные имя пользователя и пароль.
            Оба поля могут быть чувствительны к регистру.
            ''',
            'alert-danger'
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('index')
