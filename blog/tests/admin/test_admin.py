import pytest
from django.contrib.admin.sites import AdminSite
from django.test import RequestFactory
from django.contrib.auth import get_user_model # Importamos o gerenciador de usuários
from blog.admin import PostAdmin
from blog.models import Post

User = get_user_model()

@pytest.mark.django_db
def test_admin_save_model_generates_slug():
    """Garante que o Admin gera um slug automaticamente se deixado em branco."""
    
    admin_instance = PostAdmin(Post, AdminSite())
    request = RequestFactory().get('/admin/')
    
    # 1. Criamos um usuário em banco de dados especificamente para o teste
    user = User.objects.create(username="autor_teste", email="teste@mercado.com")
    
    # 2. Simulamos que este usuário está fazendo a requisição logado
    request.user = user 
    
    # 3. Adicionamos o 'author=user' na criação do Post
    new_post = Post(title="Meu Primeiro Post Moderno", content="Conteúdo teste", author=user)
    
    # Simulamos o Admin salvando o modelo
    admin_instance.save_model(request, new_post, form=None, change=False)
    
    # Verificamos se a nossa lógica funcionou
    assert new_post.slug == "meu-primeiro-post-moderno"
    assert Post.objects.count() == 1
