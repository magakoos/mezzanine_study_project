# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from mezzanine.pages.models import Page

# Create your models here.


@python_2_unicode_compatible
class ContactPage(Page):
    """
    Кастомная страница контактов. Рендерится из template_name.
    """
    template_name = 'pages/ContactPage.html'

    contact_name = models.CharField(verbose_name=u"Имя", max_length=128)
    contact_surname = models.CharField(verbose_name=u"Фамилия", max_length=128)
    email = models.EmailField(verbose_name=u"Email")
    phone = models.CharField(verbose_name=u"Телефон, №", max_length=11)

    def __str__(self):
        return u"{title}: {name} {surname}".format(
            title=self.title,
            name=self.contact_name,
            surname=self.contact_surnamel
        )

    def get_template_name(self):
        return self.template_name

