from django.contrib import admin
from .models import Post, Comment, Category, SubCategory, Link, Email


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_id', 'sub_category', 'publish', 'author',
                    'slug', 'status', 'created', 'updated')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created',
                    'post', 'active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('class_category', 'post_category')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('choice',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created', 'updated')


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')


