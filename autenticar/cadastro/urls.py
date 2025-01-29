# cadastro/urls.py
from django.urls import path
from .views import cadastrar, sucesso

urlpatterns = [
    path('', cadastrar, name='home'),  # URL para a página inicial do cadastro
    path('cadastrar/', cadastrar, name='cadastrar'),  # URL para a página de cadastro
    path('sucesso/', sucesso, name='sucesso'),  # URL para a página de sucesso
]