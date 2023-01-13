from django.db import models

from django.contrib.auth.models import (
    AbstractUser, BaseUserManager
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class MyUser(AbstractUser):

    TYPE_USER = [('ad', 'Administrador'), ('co', 'Colaborador'), ('us', 'Usuário Padrão')]
    type_user = models.CharField('type user', max_length=2, choices=TYPE_USER) 
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'type_user', 'is_active']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['first_name']

    def __str__(self):
        return self.email