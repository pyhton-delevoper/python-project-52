from django.contrib.auth.models import AbstractUser as U
from django.conf import settings


class User(U):

    def __str__(self):
        return self.get_full_name()
