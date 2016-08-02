from django.contrib import admin
from .models import User

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'is_staff']
    search_fields = ['username', 'name', 'email']

admin.site.register(User, UsuarioAdmin)
