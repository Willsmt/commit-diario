from django.contrib import admin
from .models import Post, Comment

# Configurando os comentários na mesma tela do Post
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'author','status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content')
    
    # Preenchimento automático do slug na interface visual do Admin
    prepopulated_fields = {'slug': ('title',)}

    inlines = [CommentInline]
