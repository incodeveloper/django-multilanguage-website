# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Page(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title', null=False, blank=False)
    content = CKEditor5Field('Content', config_name='extends')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HeaderSection(models.Model):

    class Meta:
        verbose_name_plural = 'Header Section'

    
    title = models.CharField(max_length=100, verbose_name='Title', blank=False, null=False)
    alt = models.CharField(max_length=100, verbose_name='Alt', blank=False, null=False)
    detail = models.TextField(verbose_name='Detail', blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class HeaderSplitText(models.Model):

    class Meta:
        verbose_name_plural = 'Split Text'

    
    text = models.CharField(max_length=80, verbose_name='Text', blank=False, null=False)
    section = models.ForeignKey(HeaderSection, related_name='header_section', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Resume(models.Model):

    title = models.CharField(max_length=100, verbose_name='Title', blank=False, null=False)
    alt = models.CharField(max_length=100, verbose_name='Alt', blank=False, null=False)
    detail = models.TextField(verbose_name='Detail', blank=False, null=False)
    resume = models.FileField(verbose_name='CV', blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Service(models.Model):

    title = models.CharField(max_length=100, verbose_name='Title', blank=False, null=False)
    detail = models.TextField(verbose_name='Detail', blank=False, null=False)
    icon = models.ImageField(verbose_name='Icon', blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):

    detail = models.TextField(verbose_name='Text', blank=False, null=False)
    name = models.CharField(max_length=100, verbose_name='Name', blank=False, null=False)
    location = models.CharField(max_length=100, verbose_name='Location', blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class VideoSection(models.Model):


    class Meta:
        verbose_name_plural = 'Video Section'
        
    title = models.CharField(max_length=255, verbose_name='Name', blank=False, null=False)
    detail = models.TextField(verbose_name='Detail', blank=False, null=False)
    video = models.TextField(verbose_name='Embed Code', blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title