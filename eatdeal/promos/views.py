from django.conf import settings
from django.shortcuts import render

from .services.promo_markers import PromoMarkers


def current_promos(request):
    city: str = request.GET.get('city') or settings.DEFAULT_CITY
    promos: str = request.GET.get('promos')
    cls = PromoMarkers(city)
    if promos == 'all':
        data = cls.get_all()
    else:
        data = cls.get_current()
    context = {
        'GOOGLE_API': settings.GOOGLE_API,
        'promos': data,
        'city': city
    }
    return render(request, 'promos/index.html', context)
