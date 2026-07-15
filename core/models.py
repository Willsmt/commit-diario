from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Tornamos o e-mail único e obrigatório para futuras integrações de API
    email = models.EmailField('email address', unique=True)
    bio = models.TextField(blank=True, null=True)

    # Definimos que o e-mail pode ser usado como identificador se necessário
    def __str__(self):
        return self.email or self.username
