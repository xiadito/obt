from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_experimentos, name='lista_experimentos'),
    path('experimento/<int:pk>/', views.detalhe_experimento, name='detalhe_experimento'),
]