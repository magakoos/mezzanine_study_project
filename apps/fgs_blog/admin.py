# coding=utf-8
from django.contrib import admin
from .models import Article, Author, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('header', 'body', 'create_date', 'change_date')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)

