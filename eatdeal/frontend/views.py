from django.conf import settings
from django.shortcuts import render


def index(request):
    context = {
        'GOOGLE_API': settings.GOOGLE_API,
        'DEFAULT_CITY': settings.DEFAULT_CITY
    }
    return render(request, 'index.html', context)
