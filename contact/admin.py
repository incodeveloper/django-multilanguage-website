from django.contrib import admin

from .models import *


class ContactAdmin(admin.ModelAdmin):

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
