from django.contrib import admin
from django.utils.text import slugify
from .models import Post, Comment

# Configurando os comentários na mesma tela do Post
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content')
    
    inlines = [CommentInline]

    # Interceptando o salvamento apenas para o slug (foco da Aula 3)
    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)
