# coding=utf-8

from django.contrib.auth.backends import ModelBackend as BaseModelBackend

from.models import User

class ModelBackend(BaseModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                if user.checkpassword(password):
                    return user
            except User.DoesNotExist:
                pass
