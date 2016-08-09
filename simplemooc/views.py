# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage
from .models import Course, Category, Modules, Teacher
from .forms import category_form, module_form, teacher_form, course_form
from django.core.mail import send_mail
from django.conf import settings
from .forms import contact_form

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'index.html'

class CourseView(generic.ListView):
    template_name = 'courses.html'
    context_object_name = 'courses'
    paginate_by = 1

    def get_queryset(self):
        queryset = Course.objects.filter(is_approved=True)
        q = self.request.GET.get('q', None)
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

class ShowCourseView(generic.DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_detail.html'

class ShowCategoryView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category.html'
    #falta carregar os cursos para a variável courses.

class CreateCategory(generic.CreateView):
    model = Category
    form_class = category_form
    template_name = 'category_form.html'

class CreateModule(generic.CreateView):
    model = Modules
    form_class = module_form
    template_name = 'module_form.html'

class CreateTeacher(generic.CreateView):
    model = Teacher
    form_class = teacher_form
    template_name = 'teacher_form.html'

class CreateCourse(generic.CreateView):
    model = Course
    form_class = course_form
    template_name = 'course_form.html'

class UpdateCourse(generic.UpdateView):
    model = Course
    form_class = course_form
    template_name = 'course_form.html'

class DeleteCourse(generic.DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('simplemooc:courses')

class ContactView(generic.FormView):
   template_name = 'contact.html'
   form_class = contact_form
   success_url = reverse_lazy('simplemooc:contact')

   def form_valid(self, form):
    subject = '[simplemooc] {} entrou em contato'.format(form.cleaned_data['name'])
    message = 'E-mail: {}\n{}'.format(
        form.cleaned_data['email'], form.cleaned_data['message']
    )
    send_mail(
        subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL]
    )
    return super(ContactView, self).form_valid(form)
