from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .services.promo_markers import PromoMarkers


def index(request):
    city: str = request.GET.get('city') or settings.DEFAULT_CITY
    selection: str = request.GET.get('selection')
    if selection == 'all':
        markers = PromoMarkers(city).get_all()
    else:
        markers = PromoMarkers(city).get_current()
    context = {
        'GOOGLE_API': settings.GOOGLE_API,
        'markers': markers,
        'city': city
    }
    return render(request, 'promos/index.html', context)
