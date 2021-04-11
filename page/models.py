# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Page(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title', null=False, blank=False)
    content = CKEditor5Field('Content', config_name='extends')

    def __str__(self):
        return self.title
