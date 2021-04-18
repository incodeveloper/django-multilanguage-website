from django.shortcuts import render
from .models import Contact

def site_contact(request):

    context = {
        'content': Contact.objects.first()
    }

    return render(request, 'contact.html', context)