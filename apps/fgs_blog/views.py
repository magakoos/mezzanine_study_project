# coding=utf-8
# from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article
# Create your views here.


class ArticleList(ListView):
    """
    Список статей для главной страницы.

    """
    model = Article
    context_object_name = 'articles'
    paginate_by = 6
    template_name = 'article_paginated_list.html'

    def get_queryset(self):
        """
        Выводит последние созданые статьи
        """
        qs = Article.objects.order_by('-create_date')
        return qs


class ArticleDetail(DetailView):
    """
    Открытая статья
    """
    model = Article
    # queryset = Article.objects.all()
    context_object_name = 'article'
    template_name = 'article_detail.html'



