from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Project
# Create your views here.

def home(request):
    return render(request, 'home.html')

def assets(request):
    return render(request, 'projects/assets.html')

def asset_create(request):
    return render(request, 'asset_create.html')