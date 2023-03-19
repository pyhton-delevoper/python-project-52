from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


def index(request, *args, **kwargs):
    message = messages.get_messages(request)
    return render(
        request, 'index.html', {'messages': message}
    )


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request):
        messages.add_message(
            request, messages.SUCCESS,
            'Вы разлогинены', 'alert-info'
        )
        return super().dispatch(request)
