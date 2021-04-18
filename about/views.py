from django.shortcuts import render
from .models import About
from page.models import Resume

def site_about(request):

    context = {
        'about': About.objects.first(),
        'resume': Resume.objects.first()
    }

    return render(request, 'about.html', context)