from django.contrib.auth.models import AbstractUser as U


class User(U):

    def __str__(self):
        return self.get_full_name()
