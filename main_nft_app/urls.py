from django.urls import path
from . import views

urlpatterns = [
# define all app-level URLS in this list
    path('', views.home, name='home'),  
]
