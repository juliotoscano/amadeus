# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Teacher, Modules, Course

# Register your models here.
admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(Modules)
admin.site.register(Course)
