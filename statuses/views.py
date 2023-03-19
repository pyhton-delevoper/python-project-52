from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class StatusesIndex(LoginRequiredMixin, View):

    permission_denied_message = 'Вы не авторизованы! Пожалуйста, выполните вход.'