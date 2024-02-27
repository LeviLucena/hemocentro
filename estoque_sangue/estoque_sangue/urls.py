# estoque_sangue/urls.py
from django.contrib import admin
from django.urls import path
from estoque import views as estoque_views

urlpatterns = [
    path('', estoque_views.login_view, name='login'),  # Rota padrão para a página de login
    path('estoque/', estoque_views.estoque_view, name='estoque'),  # Rota para a página de estoque
    path('tabela/', estoque_views.tabela_view, name='tabela'),  # Rota para a página de tabela
    path('graficos/', estoque_views.graficos_view, name='graficos'),  # Rota para a página de gráficos
    path('mapa/', estoque_views.exportar_view, name='mapa'),  # Rota para a página de exportar
    path('admin/', admin.site.urls),
    # Adicione outras rotas conforme necessário
]
