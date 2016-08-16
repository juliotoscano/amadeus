# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/add/$', views.CreateUser.as_view(), name='createUser'),
    url(r'^edit/$', views.Edit_user, name='edit_user'),
    url(r'^courses/student/$', views.CoursesStudent.as_view(), name='student_courses'),
]