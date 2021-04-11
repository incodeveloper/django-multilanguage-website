# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def site_index(request):
    return render(request, 'index.html', {})

def site_about(request):
    return render(request, 'about.html', {})

def site_contact(request):
    return render(request, 'contact.html', {})