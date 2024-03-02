# estoque/urls.py
from django.urls import path
from .views import inserir_registro
from . import views

urlpatterns = [
    path('', views.get_blood_types, name='estoque'),  # Certifique-se de que esta função existe em views.py
    path('tabela/', views.tabela_view, name='tabela'),  # Rota para a página de tabela
    path('graficos/', views.graficos_view, name='graficos'),  # Rota para a página de gráficos
    path('mapa/', views.exportar_view, name='mapa'),  # Rota para a página de exportar
    path('inserir_registro/', views.inserir_registro, name='inserir_registro'),
]
