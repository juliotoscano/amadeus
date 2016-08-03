# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from simplemooc import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^courses$', views.CourseView.as_view(), name='courses'),
    url(r'^course/([\w_-]+)/$', views.detail, name='detail'),
    url(r'^course/category/([\w_-]+)/$', views.category, name='category'),
    url(r'^registercategory/$', views.post_create_category, name='createCategory'),
    url(r'^registermodule/$', views.post_create_module, name='createModule'),
    url(r'^registerteacher/$', views.post_create_teacher, name='createTeacher'),
    url(r'^registercourse/$', views.post_create_course, name='createCourse'),
    url(r'^contact$', views.contact, name='contact'),
]