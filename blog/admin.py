from django.contrib import admin
from .models import Post, Comment,PostSubscriber
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_id', 'publish', 'author',
                    'slug', 'status', 'created', 'updated')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created',
                    'post', 'active')

@admin.register(PostSubscriber)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created',)