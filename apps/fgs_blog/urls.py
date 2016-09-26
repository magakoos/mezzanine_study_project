from django.conf.urls import url
from .views import ArticleList, ArticleDetail


urlpatterns = [
    url(r'^$', ArticleList.as_view(), ),
    url(r'^page/(?P<page>\d+)/$', ArticleList.as_view(),name='page'),
    url(r'^detail/(?P<pk>\d+)$', ArticleDetail.as_view(),name='detail'),
]