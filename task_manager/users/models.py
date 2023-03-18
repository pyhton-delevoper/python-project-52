from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class MyUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='myusers_permissions'
)