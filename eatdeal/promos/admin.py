from django.contrib import admin
from .models import *


admin.site.register([Tag, City, Cafe, Day])


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cafe')
    list_filter = ('cafe', 'cafe__city', 'days', 'is_active', 'tags')
    search_fields = ('title', 'description')
    ordering = ('title',)
    filter_horizontal = ('tags', 'days')


