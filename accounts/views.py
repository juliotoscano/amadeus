# coding=utf-8
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rolepermissions.shortcuts import assign_role
from rolepermissions.verifications import has_permission
from .forms import UserForm
from .models import User

# Create your views here.
class CreateUser(generic.CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'

    def form_valid(self, form):
        form.save()
        assign_role(form.instance, 'teacher')
        context = self.get_context_data(form=form)
        context['success']= True
        return self.render_to_response(context)

@login_required
def edit_user(request):
    form = UserForm(data=request.POST or None, instance=request.user)
    context = {}

    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, 'edit.html', context)
