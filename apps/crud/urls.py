from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('novo-paciente/', views.novo_paciente, name='novo_paciente'),
]