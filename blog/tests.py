import pytest
from .factories import PostFactory

# O marcador @pytest.mark.django_db dá permissão para o teste acessar o banco temporário
@pytest.mark.django_db
def test_post_foi_criado_com_sucesso():
    # ARRANGE & ACT: Criamos um post. Note que não passamos 'author', 
    # o FactoryBoy cria o usuário automaticamente em background!
    post = PostFactory(title="Dominando o Pytest", slug="dominando-o-pytest")

    # ASSERT: Verificamos se deu tudo certo usando Python puro
    assert post.title == "Dominando o Pytest"
    assert post.slug == "dominando-o-pytest"
    assert post.status == 1
    
    # Verificando se o relacionamento funcionou (o usuário deve ter um nome gerado pela fábrica)
    assert post.author.username.startswith("usuario")

@pytest.mark.django_db
def test_post_str_retorna_o_titulo():
    post = PostFactory(title="Meu Diário de Código")
    assert str(post) == "Meu Diário de Código"
