from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from .models import Solicitud

# Create your views here.


class SolicitudBaseView(View):
    template_name = 'solicitud.html'
    model = Solicitud 
    fields = '__all__'
    success_url = reverse_lazy('solicitud:all')
    
class SolicitudListView(SolicitudBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LAS SOLICTUDES
    """
    
class SolicitudDetailView(SolicitudBaseView,DetailView):
    template_name = "solicitud_detail.html"
    
class SolicitudCreateView(SolicitudBaseView,CreateView):
    template_name = "solicitud_create.html"
    extra_context = {
        "tipo": "Crear solicitud"
    }


class SolicitudUpdateView(SolicitudBaseView,UpdateView):
    template_name = "solicitud_create.html"
    extra_context = {
        "tipo": "Actualizar solicitud"
    }

class SolicitudDeleteView(SolicitudBaseView,DeleteView):
    template_name = "solicitud_delete.html"
    extra_context = {
        "tipo": "Borrar solicitud"
    }