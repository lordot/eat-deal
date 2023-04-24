from django.conf import settings
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, Promo
from .services.promo_markers import PromoMarkers


class CityView(APIView):

    def get(self, request):
        return Response(list(City.objects.all().values('name')))


class PromoView(APIView):

    def get(self, request):
        cls = PromoMarkers(
            request.GET.get('city', settings.DEFAULT_CITY),
            self.request.user
        )
        if request.GET.get('selection') == 'all':
            data = cls.get_all()
        else:
            data = cls.get_current()
        return Response(data)


class PromoFavoriteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        return get_object_or_404(Promo, pk=pk)

    def post(self, request, pk):
        self.request.user.favorites.add(self.get_object(pk))
        return Response('favored!')

    def delete(self, request, pk):
        self.request.user.favorites.remove(self.get_object(pk))
        return Response('unfavored!')


