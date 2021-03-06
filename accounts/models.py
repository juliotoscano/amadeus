# coding=utf-8

from __future__ import unicode_literals

import re
# from django.contrib.auth.models import User
from django.db import models
from simplemooc.models import Course
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Usuario', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
                )
        ],  help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=True)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)
    subscription = models.ManyToManyField(Course, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]




