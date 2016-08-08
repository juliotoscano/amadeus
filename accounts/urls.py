# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/add/$', views.CreateUser.as_view(), name='createUser'),
    url(r'^edit/$', views.edit_user, name='edit_user'),
]