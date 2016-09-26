# coding=utf-8

from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from mezzanine.pages.admin import PageAdmin
# Register your models here.
from .models import ContactPage

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, 'image')
blog_fieldsets[0][1]["fields"].insert(-2, 'annotation')


class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

    class Meta:
        verbose_name = 'Кастомный блог'


class ContactPageAdmin(PageAdmin):
    class Meta:
        verbose_name = 'Контакт'


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
