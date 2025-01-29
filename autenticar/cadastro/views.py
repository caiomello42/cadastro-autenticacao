# cadastro/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm

def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            user = User.objects.create_user(
                username=usuario.nome,  # Use um campo apropriado para o nome de usuário
                email=usuario.email,
                password='default_password'  # Defina uma senha padrão ou obtenha do formulário
            )
            usuario.user = user  # Associa o usuário ao modelo Usuario
            usuario.save()  # Salva o modelo Usuario

            return redirect('sucesso')  # Redireciona para a página de sucesso
    else:
        form = UsuarioForm()

    return render(request, 'index.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')  # Renderiza a página de sucesso