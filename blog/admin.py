from django.contrib import admin
from .models import Post, Blog, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'create_time')
    list_filter = [('create_time')]
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = [('title')]

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
