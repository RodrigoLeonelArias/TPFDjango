from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'inicio.html'
    
class Api(TemplateView):
    template_name = 'api.html'
    context_object_name = 'api_data'