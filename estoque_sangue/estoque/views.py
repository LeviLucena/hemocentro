# estoque/views.py
from django.shortcuts import render, redirect
from .models import EstoqueSangue
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('estoque')  # Redireciona para a página de estoque após o login bem-sucedido
        else:
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
    return render(request, 'login.html')

def processar_formulario(request):
    if request.method == 'POST':
        hemocentro = request.POST.get('hemocentro')
        tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        
        for tipo_sanguineo in tipos_sanguineos:
            estoque_atual = request.POST.get(f'{tipo_sanguineo}_stock')
            estoque_minimo = request.POST.get(f'{tipo_sanguineo}_min')

            # Crie uma instância do modelo EstoqueSangue e salve no banco de dados
            estoque = EstoqueSangue(hemocentro=hemocentro, tipo_sanguineo=tipo_sanguineo, estoque_atual=estoque_atual, estoque_minimo=estoque_minimo)
            estoque.save()

        # Redirecione para a página de sucesso ou faça qualquer outra coisa que desejar
        return redirect('pagina_sucesso')
    
    return render(request, 'estoque.html')

def estoque_view(request):
    if request.method == 'POST':
        hemocentro = request.POST.get('hemocentro')
        tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        
        for tipo_sanguineo in tipos_sanguineos:
            estoque_atual = request.POST.get(f'{tipo_sanguineo}_stock')
            estoque_minimo = request.POST.get(f'{tipo_sanguineo}_min')

            # Crie uma instância do modelo EstoqueSangue e salve no banco de dados
            estoque = EstoqueSangue(hemocentro=hemocentro, tipo_sanguineo=tipo_sanguineo, estoque_atual=estoque_atual, estoque_minimo=estoque_minimo)
            estoque.save()

        # Redirecione para a página de sucesso ou faça qualquer outra coisa que desejar
        return redirect('pagina_sucesso')
    
    return render(request, 'estoque.html')

def tabela_view(request):
    return render(request, 'tabela.html')

def graficos_view(request):
    return render(request, 'graficos.html')

def exportar_view(request):
    return render(request, 'mapa.html')



