from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_experimentos, name='lista_experimentos'),
    path('experimento/<int:experimento_id>/', views.detalhe_experimento, name='detalhe_experimento'),
]