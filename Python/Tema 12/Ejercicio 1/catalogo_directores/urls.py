from django.urls import path
from . import views

urlpatterns = [
    path('', views.peliculas, name='index')
]