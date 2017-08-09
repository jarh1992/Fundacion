#creado por jesus

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Administrador, Usuario, Fundacion

# Create your views here.
def index(request):
	template = loader.get_template('base.html')
	context = {}
	return HttpResponse(template.render(context, request))


def index1(request):
	template = loader.get_template('index.html')
	fund = Fundacion.objects.get(Num_id=123)
	#admin = Administrador.objects.get()
	context = {
		'fund_name': fund.Nom
		#'admin_name': admin.Nom
		}
	return HttpResponse(template.render(context, request))


def index2(request):
	template = loader.get_template('index2.html')
	context = {}
	return HttpResponse(template.render(context, request))
