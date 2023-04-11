from datetime import datetime

from django.db.models import QuerySet, Exists, OuterRef
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from api.models import City, Promo
from api.serializers import PromoSerializer


class PromoMarkers:
    """Класс маркеров для карты."""

    def __init__(self, city: str, user, serializer=PromoSerializer):
        self.city: City = get_object_or_404(City, name=city)
        self.serializer: serializers = serializer
        self.queryset: QuerySet = self._get_queryset(user)

    def _get_queryset(self, user):
        qs: QuerySet = Promo.objects.select_related(
            'cafe'
        ).prefetch_related('tags', 'days').filter(
            cafe__city__name=self.city.name
        )
        if user.is_authenticated:
            return qs.annotate(
                is_favorited=Exists(Promo.objects.filter(
                    favorited=user.id, id=OuterRef('id')))
            )
        return qs

    def get_current(self) -> list:
        """Метод получения активных маркеров на текущее момент."""
        now: datetime = datetime.now(self.city.utc_time)
        time: str = now.strftime("%H:%M")
        day: str = now.strftime('%A')
        promos: QuerySet = self.queryset.filter(
            start_time__lte=time,
            end_time__gte=time,
            days__name=day
        )
        return self.serializer(promos, many=True).data

    def get_all(self) -> list:
        """Получение всех маркеров."""
        return self.serializer(self.queryset, many=True).data


