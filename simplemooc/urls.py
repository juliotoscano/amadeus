# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from simplemooc import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^courses/$', views.CourseView.as_view(), name='courses'),
    url(r'^course/(?P<slug>[\w_-]+)/$', views.ShowCourseView.as_view(), name='detail'),
    url(r'^course/category/(?P<slug>[\w_-]+)/$', views.ShowCategoryView.as_view(), name='category'),
    url(r'^category/add/$', views.CreateCategory.as_view(), name='createCategory'),
    url(r'^module/add$', views.CreateModule.as_view(), name='createModule'),
    url(r'^teacher/add$', views.CreateTeacher.as_view(), name='createTeacher'),
    url(r'^course/add$', views.CreateCourse.as_view(), name='createCourse'),
    url(r'^course/update/(?P<slug>[\w_-]+)/$', views.UpdateCourse.as_view(), name='updateCourse'),
    url(r'^course/delete/(?P<slug>[\w_-]+)/$', views.DeleteCourse.as_view(), name='deleteCourse'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
]
