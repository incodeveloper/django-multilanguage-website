# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    class Meta:
        model = Page


admin.site.register(Page, PageAdmin)