from django.shortcuts import render
from django.views.generic import *
from .models import *
# Create your views here.
class HomePage(ListView):
    model = Data
    template_name='home.html'
    context_object_name='data'
