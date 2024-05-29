from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Experimento

def lista_experimentos(request):
    experimentos = Experimento.objects.all()
    content = {'experimentos': experimentos}
    return render(request, 'obt_pr/experimentos.html', content)

def detalhe_experimento(request, experimento_id):
    experimento = get_object_or_404(Experimento, pk=experimento_id)
    content = {'experimentos': experimentos}
    return render(request, 'obt_pr/detalhe_experimento.html', content)