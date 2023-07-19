from django.contrib import admin

from blog.models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'slug', 'author', 'publish', 'status'] #отображение
    list_filter = ['status', 'created', 'publish', 'author'] #фильтрация
    search_field = ['title', 'body'] # поиск по значениям
    prepopulated_fields = {'slug':('title',)} # автозаполнение
    raw_id_fields = ['author'] #отображение виджета для выбора пользователя
    date_hierarchy = 'publish' #навигация по иерархии дат
    ordering = ['status', 'publish'] #упорядочение
    # list_editable = ['status']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']

