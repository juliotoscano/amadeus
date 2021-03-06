# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Category, Modules, Teacher, Course

class contact_form(forms.Form):
    name = forms.CharField(label='nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

class category_form(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug'
        ]

class module_form(ModelForm):
    class Meta:
        model = Modules
        fields = [
            'name',
            'slug',
            'description',
            'material',
            'activities',
            'is_visible'
        ]

class teacher_form(ModelForm):
    class Meta:
        model = Teacher
        fields = [
        'name',
        'slug'
        ]

class course_form(ModelForm):
    class Meta:
        model = Course
        fields =[
        'name',
        'slug',
        'description',
        'program',
        'qtd_available',
        'qtd_students',
        'begin_matric',
        'end_matric',
        'begin_course',
        'end_course',
        'image',
        'is_approved',
        'teacher',
        'category',
        'modules',
        'keywords'
        ]
