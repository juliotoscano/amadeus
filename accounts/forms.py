# coding=utf-8

from django import forms

from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha',widget=forms.PasswordInput)

    def save(self, commit=True):
        super(UserForm, self).save(commit=False)
        self.instance.set_password(self.cleaned_data['password'])
        self.instance.save()
        return self.instance

    class Meta:
        model =User
        fields = ['username', 'password', 'email']