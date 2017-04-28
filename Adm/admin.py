from django.contrib import admin
from .models import Administrador, Fundacion, Usuario

# Register your models here.
admin.site.register(Administrador, Fundacion, Usuario)