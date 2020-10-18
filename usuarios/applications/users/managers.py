from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **kwargs):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **kwargs):
        return self._create_user(username, email, password, False, False, **kwargs)

    def create_superuser(self, username, email, password=None, **kwargs):
        return self._create_user(username, email, password, True, True, **kwargs)
