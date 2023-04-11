from rest_framework import serializers

from api.models import Promo


class PromoSerializer(serializers.ModelSerializer):
    cafe = serializers.CharField(source='cafe.name')
    is_favorited = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = Promo
        fields = ['title', 'description', 'start_time', 'end_time', 'cafe', 'is_favorited']
