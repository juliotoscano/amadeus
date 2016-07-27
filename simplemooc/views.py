# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from .models import Course, Category, Modules
from .forms import category_form, module_form, teacher_form, course_form
# Create your views here.

def home(request):
    context = {}
    return render(request, 'index.html', context)

def courses(request):
    context = {}
    courses = Course.objects.all()
    context['courses'] = courses
    return render(request, 'courses.html', context)

def detail(request, slug):
    context = {}
    course = get_object_or_404(Course, slug=slug)
    context['course'] = course
    return render(request,'course_detail.html', context)

def category(request, slug):
    context = {}
    category = get_object_or_404(Category, slug=slug)
    context['category'] = category
    context['courses'] = category.courses.filter()
    return render(request,'category.html', context)

def post_create_category(request):
    context = {}
    form = category_form(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request,'categoryForm.html', context)

def post_create_module(request):
    context = {}
    form = module_form(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request,'moduleForm.html', context)

def post_create_teacher(request):
    context = {}
    form = teacher_form(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request,'teacherForm.html', context)

def post_create_course(request):
    context = {}
    form = course_form(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request,'courseForm.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)