# coding=utf-8

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views import generic

from fgs_blog.views import ArticleList, ArticleDetail


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', generic.TemplateView.as_view(template_name='base.html')),
    url(r'^', include('mezza.urls')),
    url(r'^fgs_blog/', include('fgs_blog.urls')),

]
if settings.TEMPLATE_DEBUG:
    urlpatterns += [
        url(r'^404.html$', generic.TemplateView.as_view(template_name='404.html')),
        url(r'^500.html$', generic.TemplateView.as_view(template_name='500.html')),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
