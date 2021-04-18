from django.contrib import admin

from .models import *


class AboutAdmin(admin.ModelAdmin):

    class Meta:
        model = About


admin.site.register(About, AboutAdmin)
