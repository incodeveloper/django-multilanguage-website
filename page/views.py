# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

def site_index(request):

    header_section = HeaderSection.objects.first()
    split_text = HeaderSplitText.objects.select_related('section').all()
    resume = Resume.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    video = VideoSection.objects.first()

    context = {
        'header_section': header_section,
        'split_text': split_text,
        'resume': resume,
        'services': services,
        'testimonials': testimonials,
        'video': video
    }

    return render(request, 'index.html', context)
