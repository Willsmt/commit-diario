from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Colunas que vão aparecer na listagem do painel
    list_display = ('title', 'slug', 'status', 'created_on')
    
    # Filtros laterais para facilitar a busca
    list_filter = ('status', 'created_on')
    
    # Barra de pesquisa para buscar posts por título ou conteúdo
    search_fields = ['title', 'content']
    
    # Preenche o campo 'slug' automaticamente enquanto você digita o título!
    prepopulated_fields = {'slug': ('title',)}
