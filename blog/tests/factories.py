import factory
from django.contrib.auth.models import User
from blog.models import Post

# Fábrica de Usuários
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # O Sequence garante que cada usuário gerado terá um nome único (usuario0, usuario1...)
    username = factory.Sequence(lambda n: f'usuario{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@exemplo.com')

# Fábrica de Posts
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f'Post de Teste {n}')
    slug = factory.Sequence(lambda n: f'post-de-teste-{n}')
    content = "Conteúdo gerado automaticamente pelo Factory Boy para testes."
    status = 1
    
    # A MÁGICA: Sempre que criarmos um Post, ele automaticamente cria um User para ser o autor!
    author = factory.SubFactory(UserFactory)
