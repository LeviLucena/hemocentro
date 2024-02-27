# estoque/views.py
from django.shortcuts import render
from .forms import EstoqueForm

def estoque(request):
    form = EstoqueForm()
    return render(request, 'estoque.html', {'form': form})
