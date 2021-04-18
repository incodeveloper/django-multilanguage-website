# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class PageAdmin(admin.ModelAdmin):
    class Meta:
        model = Page


class HeaderSectionAdmin(admin.ModelAdmin):
    class Meta:
        model = HeaderSection


class HeaderSplitTextAdmin(admin.ModelAdmin):
    class Meta:
        model = HeaderSplitText


class ResumeAdmin(admin.ModelAdmin):
    class Meta:
        model = Resume


class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service


class TestimonialAdmin(admin.ModelAdmin):
    class Meta:
        model = Testimonial


class VideoSectionAdmin(admin.ModelAdmin):
    class Meta:
        model = VideoSection


admin.site.register(Page, PageAdmin)
admin.site.register(HeaderSection, HeaderSectionAdmin)
admin.site.register(HeaderSplitText, HeaderSplitTextAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(VideoSection, VideoSectionAdmin)