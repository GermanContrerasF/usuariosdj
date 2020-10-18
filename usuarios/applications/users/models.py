from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENERO_OPCIONES = (
        ('f', 'Femenino'),
        ('m', 'Masculino'),
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO_OPCIONES, blank=True)
    is_staff = models.BooleanField(default=False)    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return f'{self.nombres} {self.apellidos}'
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

