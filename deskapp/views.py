"""
testing
"""
from django.shortcuts import render

# Create your views here.
def landing (request):
    """Pagina de Inicio"""
    return render(request, 'landing.html')
