from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Administrador, Usuario

# Create your views here.
def index(request):
	template = loader.get_template('base.html')
	context = {}
	return HttpResponse(template.render(context, request))