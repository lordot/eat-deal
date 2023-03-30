from django.conf import settings
from django.core import serializers
from django.shortcuts import render

from .models import Promo


def index(request):
    promos = Promo.objects.select_related('cafe').prefetch_related('tags', 'days')
    data = serializers.serialize('json', promos, use_natural_foreign_keys=True)
    return render(request, 'promos/index.html', {
        'GOOGLE_API': settings.GOOGLE_API,
        'promos': data
    })
