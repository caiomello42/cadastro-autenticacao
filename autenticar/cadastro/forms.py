from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)  # Usar um campo de senha

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        # Cria um usuário do Django
        user = User(username=usuario.nome, email=usuario.email)  # Use o nome ou crie um campo para username
        user.set_password(self.cleaned_data['senha'])  # Define a senha
        if commit:
            user.save()  # Salva o usuário no banco de dados
            usuario.user = user  # Associa o usuário ao modelo Usuario
            usuario.save()  # Salva o modelo Usuario
        return usuario