from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Importe o seu modelo de usuário customizado

# Registra o seu modelo no Admin com a configuração de visualização padrão do Django
admin.site.register(User, UserAdmin)
