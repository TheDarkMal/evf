from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evento, espacios, EspacioOtro
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class cargar_inicio(ListView):
    model = Evento
    template_name = "EventViewApp/inicio.html"
    
class EventoList(ListView):
    model = Evento
    template_name = 'EventViewApp/lista_eventos.html'


class EventoCreate(LoginRequiredMixin,CreateView):
    model = Evento
    fields = ['nombre','descripcion','empresa','fecha','imagen']
    template_name = 'EventViewApp/nuevo_evento.html'
    success_url = reverse_lazy('lista_eventos')
    
class ListaEventos(ListView):
    model = Evento
    template_name = 'EventViewApp/Lista_eventos.html'



class agregarList(ListView):
    model = Evento
    template_name = 'EventViewApp/agregar.html'


class EventoDelete(DeleteView):
    model = Evento
    fields = ['nombre','descripcion','empresa','fecha','imagen']
    template_name = 'EventViewApp/eliminar_evento.html'
    success_url = reverse_lazy('lista_eventos')


class NosotrosList(ListView):
    model = Evento
    template_name = 'EventViewApp/nosotros.html'

class espacioss(ListView):
    model = Evento
    template_name = 'EventViewApp/agregar_espacio.html'

class serviciosS(ListView):
    model = Evento
    template_name = 'EventViewApp/agregar_servicios.html'

class RegistroUsuarios(CreateView):
    model = User
    template_name = 'EventViewApp/registrarusuario.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('inicio')

class NuevoEspacioo(CreateView):
    model = EspacioOtro
    fields = ['nombre','casaEventos','descripcion','precio']
    template_name = 'EventViewApp/Espacio_nuevo.html'
    success_url = reverse_lazy('agregar')

class NuevoServicio(CreateView):
    model = espacios
    fields = ['nombre','descripcion','precio']
    template_name = 'EventViewApp/Servicio_nuevo.html'
    success_url = reverse_lazy('agregar')