from rest_framework import serializers
from .models import Promo


class PromoSerializer(serializers.ModelSerializer):
    cafe = serializers.CharField(source='cafe.name')
    city = serializers.CharField(source='cafe.city')

    class Meta:
        model = Promo
        fields = ['title', 'description', 'start_time', 'end_time', 'cafe', 'city']
