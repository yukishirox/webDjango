from django.urls import path
from perfil.views import perfil_inicio


urlpatterns = [
    path('', login_required(perfil_inicio), name='perfil_inicio'),
]