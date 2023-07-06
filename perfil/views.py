from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.

def perfil_inicio(request):
    # Código de la vista perfil_inicio
    return HttpResponse("Página de inicio de perfil")