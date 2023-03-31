from datetime import datetime

from django.conf import settings
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from ..serializers import PromoSerializer
from ..models import Promo, City
from rest_framework import serializers


class PromoMarkers:
    """Класс маркеров для карты."""

    def __init__(self, city: str, serializer=PromoSerializer):
        self.city: City = get_object_or_404(City, name=city)
        self.serializer: serializers = serializer
        self.queryset: QuerySet = Promo.objects.select_related('cafe').prefetch_related(
            'tags', 'days'
        ).filter(cafe__city__name=self.city.name)

    def get_current(self) -> list:
        """Метод получения активных маркеров на текущее время."""
        now: datetime = datetime.now(self.city.utc_time)
        time: str = now.strftime("%H:%M")
        day: str = now.strftime('%A')
        promos: QuerySet = self.queryset.filter(
            start_time__lte=time,
            end_time__gte=time,
            days__name=day
        )
        data = self.serializer(promos, many=True).data
        return data

    def get_all(self) -> list:
        data = self.serializer(self.queryset, many=True).data
        return data
