# coding=utf-8
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import User

# Create your views here.
class CreateUser(generic.CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'


@login_required
def edit_user(request):
    form = UserForm(data=request.POST or None, instance=request.user)
    context = {}

    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, 'edit.html', context)
