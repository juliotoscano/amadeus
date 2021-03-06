# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, CreateView, ListView, FormView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
from django.conf import settings
from rolepermissions.mixins import HasRoleMixin
from .forms import category_form, module_form, teacher_form, course_form, contact_form
from .models import Course, Category, Modules, Teacher

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

class CourseView(ListView):
    template_name = 'courses.html'
    context_object_name = 'courses'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
            context['subscription'] = Course.objects.all()
        context.update(kwargs)
        return super(MultipleObjectMixin, self).get_context_data(**context)

    def get_queryset(self):
        u = self.request.user
        if u.is_authenticated():
            queryset = Course.objects.filter(user=self.request.user)
        else:
            queryset = Course.objects.all()

        q = self.request.GET.get('q', None)
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

class ShowCourseView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_detail.html'

class ShowCategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category.html'
    #falta carregar os cursos para a variável courses.

class CreateCategory(CreateView):
    model = Category
    form_class = category_form
    template_name = 'category_form.html'

class CreateModule(CreateView):
    model = Modules
    form_class = module_form
    template_name = 'module_form.html'

class CreateTeacher(CreateView):
    model = Teacher
    form_class = teacher_form
    template_name = 'teacher_form.html'

class CreateCourse(CreateView, HasRoleMixin):
    allowed_roles = [Teacher]
    model = Course
    form_class = course_form
    template_name = 'course_form.html'

class UpdateCourse(UpdateView):
    model = Course
    form_class = course_form
    template_name = 'course_form.html'

class DeleteCourse(DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('simplemooc:courses')

class ContactView(FormView):
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
