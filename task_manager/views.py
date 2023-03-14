from django.shortcuts import render
from django.views import View
from django.contrib import messages


class Index(View):

    def get(self, request, *args, **kwargs):
        message = messages.get_messages(request)
        return render(
            request, 'index.html', {'message': message})