import factory
from django.contrib.auth import get_user_model
from blog.models import Post

# Puxa dinamicamente o Custom User (core.User)
User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User # Agora a Factory aponta para a tabela certa (core_user)

    username = factory.Sequence(lambda n: f'usuario{n}')
    email = factory.Sequence(lambda n: f'usuario{n}@mercado.com')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    slug = factory.Faker('slug')
    
    # Ao criar um Post, cria um Custom User associado automaticamente
    author = factory.SubFactory(UserFactory)
