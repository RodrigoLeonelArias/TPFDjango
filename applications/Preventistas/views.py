from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Preventista
from .form import LoginForm, ProveedorForm
from rest_framework.generics import ListAPIView
from .serializer import PreventistaSerializer

from django.views.generic import (
    View,
    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView
)
from django.views.generic.edit import (
    FormView
)

############################ LOGIN ####################################
class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('preventista_app:panel-proveedor')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(ListView):
    model = Preventista
    template_name = 'preventistas/panel.html'
    context_object_name = 'proveedor'
    paginate_by = 5

    
    def get_queryset(self):
        #Definimos variables donde obtendremos los request
        
        dato = self.request.GET.get('dato','')
        #Del model Proveedor filtramos los atributos que necesitamos
        lista = (
              Preventista.objects.filter(identificador__icontains = dato) 
            | Preventista.objects.filter(nombre__icontains = dato) 
            | Preventista.objects.filter(rubro__icontains = dato)
                )
        return lista
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'preventista_app:login-proveedor'
            )
        )

############################ VISTAS GENERALES ####################################

class ProveedorDetalles(LoginRequiredMixin,DetailView):
    model = Preventista
    template_name = "preventistas/detalles.html"
    context_object_name = "detalle"
    login_url = reverse_lazy('preventista_app:login-proveedor')


class ProveedorCreateView(LoginRequiredMixin,CreateView):
    model = Preventista
    template_name = "preventistas/create.html"
    form_class = ProveedorForm
    login_url = reverse_lazy('preventista_app:login-proveedor')
    success_url = reverse_lazy('preventista_app:panel-proveedor') #una vez agregado, vuelve hacia la pag que le pasemos


class ProveedorUpdateView(LoginRequiredMixin,UpdateView):
    model = Preventista
    template_name = "preventistas/update.html"
    form_class = ProveedorForm
    login_url = reverse_lazy('preventista_app:login-proveedor')
    success_url = reverse_lazy('preventista_app:panel-proveedor') #una vez agregado, vuelve hacia la pag que le pasemos


class ProveedorDeleteView(LoginRequiredMixin,DeleteView,DetailView):
    model = Preventista
    template_name = "preventistas/delete.html"
    context_object_name = 'delete_detail'
    login_url = reverse_lazy('preventista_app:login-proveedor')
    success_url = reverse_lazy('preventista_app:panel-proveedor') #una vez agregado, vuelve hacia la pag que le pasemos


############################ LAS SIGUIENTES CLASES NOS PERMITEN DEVOLVER OBJETOS EN ORDEN ####################################

class ProveedorIdentificador(LoginRequiredMixin,ListView):
    model = Preventista
    template_name = "preventistas/panel.html"
    ordering = 'identificador'
    paginate_by = 5
    context_object_name = "proveedor"    
    #los objetos que las vistas mandan al template para ver los preventistas que tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('preventista_app:login-proveedor')


class ProveedorNombre(LoginRequiredMixin,ListView):
    model = Preventista
    template_name = "preventistas/panel.html"
    ordering = 'nombre'
    paginate_by = 5
    context_object_name = "proveedor"    
    #los objetos que las vistas mandan al template para ver los preventistas que tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('preventista_app:login-proveedor')


class ProveedorRubro(LoginRequiredMixin,ListView):
    model = Preventista
    template_name = "preventistas/panel.html"
    ordering = 'rubro'
    paginate_by = 5
    context_object_name = "proveedor"    
    #los objetos que las vistas mandan al template para ver preventistas tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('preventista_app:login-proveedor')
    
############################ API VIEW ####################################
class ProveedorListApiView(ListAPIView):

    serializer_class = PreventistaSerializer

    def get_queryset(self):
        return Preventista.objects.all()