from django.shortcuts import render
from .models import Project



def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})

from django.shortcuts import render, redirect
from .form import ProjectForms


def crear_post(request):
    if request.method == 'POST':
        form = ProjectForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirige a la vista de listado de proyectos
    else:
        form = ProjectForms()
    
    return render(request, 'administracion.html', {'form': form})


