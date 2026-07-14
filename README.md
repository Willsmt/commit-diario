# git commit -m "diário"

> Blog pessoal sobre estudos, projetos e o que aprendo sobre código e segurança pelo caminho.

Projeto desenvolvido com **Django 6.0** como parte do curso Desenvolvedor Full Stack Python (EBAC), módulo *Configurando o Django*.

## Stack

- Python 3.12+
- Django 6.0
- SQLite (desenvolvimento)
- python-decouple (variáveis de ambiente)

## Estrutura

```
django-projeto/
├── core/          # configuração do projeto (settings, urls, wsgi, asgi)
├── blog/          # app principal do blog
├── manage.py
├── .env           # variáveis sensíveis (não versionado)
└── .gitignore
```

## Rodando localmente

```bash
# 1. Clonar e entrar no diretório
git clone git@github.com:Willsmt/commit-diario.git
cd commit-diario

# 2. Criar e ativar o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências
pip install django python-decouple

# 4. Criar o arquivo .env na raiz
echo "SECRET_KEY=sua-chave-secreta-aqui" > .env
echo "DEBUG=True" >> .env

# 5. Aplicar migrações
python manage.py migrate

# 6. Criar superusuário (opcional, para acessar /admin)
python manage.py createsuperuser

# 7. Subir o servidor
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` para ver a aplicação e `http://127.0.0.1:8000/admin/` para o painel administrativo.

## Segurança

A `SECRET_KEY` e demais dados sensíveis são carregados via variáveis de ambiente (`.env`), nunca versionados no repositório.

---

Desenvolvido por [Willians](https://github.com/Willsmt) — *dev com visão de segurança*.
