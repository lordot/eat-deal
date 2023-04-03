from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from .models import City, Promo
from .serializers import PromoSerializer
from .services.promo_markers import PromoMarkers


def city_list_view(request):
    cities = City.objects.all().values('name')
    return JsonResponse(list(cities), safe=False)


class PromoViewSet(ListModelMixin, GenericViewSet):
    serializer_class = PromoSerializer
    queryset = Promo.objects.all()

    def list(self, request, *args, **kwargs):
        cls = PromoMarkers(request.GET.get('city', settings.DEFAULT_CITY))
        if request.GET.get('selection') == 'all':
            data = cls.get_all()
        else:
            data = cls.get_current()
        return Response(data)

