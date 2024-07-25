from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Cliente
from .form import LoginForm, ClienteForm
from rest_framework.generics import ListAPIView
from .serializer import ClienteSerializer


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
    success_url = reverse_lazy('cliente_app:panel-cliente')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(ListView):
    model = Cliente
    template_name = 'cliente/panel.html'
    context_object_name = 'clientes'
    paginate_by = 5

    
    def get_queryset(self):
        #definimos variables donde obtendremos los request
        dato = self.request.GET.get('dato','')
        #del model Cliente filtramos los atributos que necesitamos
        lista = Cliente.objects.filter(dni__icontains = dato) | Cliente.objects.filter(nombre__icontains = dato) | Cliente.objects.filter(apellido__icontains = dato)
        return lista
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'cliente_app:login-cliente'
            )
        )


################## VISTAS ####################
class ClienteDetalles(LoginRequiredMixin,DetailView):  #DETALLES
    model = Cliente
    template_name = "cliente/detalles.html"
    context_object_name = "detalle"
    login_url = reverse_lazy('cliente_app:login-cliente')



class ClienteCreateView(LoginRequiredMixin,CreateView):    #CREACION
    model = Cliente
    template_name = "cliente/create.html"
    form_class = ClienteForm
    login_url = reverse_lazy('cliente_app:login-cliente')
    success_url = reverse_lazy('cliente_app:panel-cliente')
    

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.nombre_completo = f"{cliente.nombre} {cliente.apellido}"
        cliente.save()

        return super(ClienteCreateView, self).form_valid(form)
    
    
class ClienteUpdateView(LoginRequiredMixin,UpdateView):    #MODIFICACION
    model = Cliente
    template_name = "cliente/update.html"
    form_class = ClienteForm
    login_url = reverse_lazy('cliente_app:login-cliente')
    success_url = reverse_lazy('cliente_app:panel-cliente')

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.nombre_completo = f"{cliente.nombre} {cliente.apellido}"
        cliente.save()

        return super(ClienteUpdateView, self).form_valid(form)


class ClienteDeleteView(LoginRequiredMixin,DeleteView,DetailView):
    model = Cliente
    template_name = "cliente/delete.html"
    context_object_name = "delete_detail"
    login_url = reverse_lazy('cliente_app:login-cliente')
    success_url = reverse_lazy('cliente_app:panel-cliente')

############## VIEWS DE ORDEN #################

class ClienteDni(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = "cliente/panel.html"
    ordering = 'dni'
    paginate_by = 5
    context_object_name = "clientes"    
    #Los objetos que las vistas mandan al template para ver los clientes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('cliente_app:login-cliente')


class ClienteNombre(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = "cliente/panel.html"
    ordering = 'nombre'
    paginate_by = 5
    context_object_name = "clientes"    
    #Los objetos que las vistas mandan al template para ver los clientes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('cliente_app:login-cliente')


class ClienteApellido(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = "cliente/panel.html"
    ordering = 'apellido'
    paginate_by = 5
    context_object_name = "clientes"    
    #Los objetos que las vistas mandan al template para ver los clientes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('cliente_app:login-cliente')
    

############################ API VIEW ####################################

class ClienteListApiView(ListAPIView):

    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all()