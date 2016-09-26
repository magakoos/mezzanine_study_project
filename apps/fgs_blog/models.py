# coding=utf-8
from django.db import models
from mezzanine.pages.models import Page
from django.utils.translation import ugettext_lazy as _

from mezzanine.blog.models import BlogPost
# Create your models here.


class Author(models.Model):
    """
    Автор статьи в блоге.
    """
    name = models.CharField(verbose_name=u"Имя", max_length=128)
    surname = models.CharField(verbose_name=u"Фамилия", max_length=128)
    email = models.EmailField(verbose_name=u"Email")
    phone = models.CharField(verbose_name=u"Телефон, №", max_length=11)

    def __unicode__(self):
        return u'{email}: {name} {surname}'.format(
            email=self.email,
            name=self.name,
            surname=self.surname
        )

    def __str__(self):
        return u"{email}: {name} {surname}".format(
            email=self.email,
            name=self.name,
            surname=self.surname
        )


class Tag(models.Model):
    """
    Тег для статьи.
    """
    name = models.CharField(verbose_name=u"Meta Tag", max_length=128)

    def __unicode__(self):
        return u"{name}".format(
            name=self.name
        )

    def __str__(self):
        return u"{name}".format(
            name=self.name
        )


class AriclePage(Page):
    """
    Страница с картинкой.
    """
    image = models.ImageField(
        upload_to='.',
        verbose_name='Картинка',
        default=None
    )
    label = models.CharField(max_length=256, verbose_name='Описание')


class Article(models.Model):
    """
    Статья в блоге.
    """
    header = models.CharField(verbose_name=u"Заголовок", max_length=128)
    body = models.CharField(verbose_name=u"Текст", max_length=8192)
    create_date = models.DateTimeField(
        verbose_name=u"Дата создания",
        auto_now_add=True
    )
    change_date = models.DateTimeField(
        verbose_name=u"Дата изменения",
        auto_now=True
    )
    authors = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag)
    images = models.ForeignKey(AriclePage)

    def __unicode__(self):
        return u'{header} написаную {author}'.format(
            header=self.header,
            author=''
        )

    def __str__(self):
        return u'{header} написаную {author}'.format(
            header=self.header,
            author=''
        )
