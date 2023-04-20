from django.contrib import admin

from .models import Cafe, City, Day, Promo, Tag

admin.site.register([Tag, City, Cafe, Day])


class PromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'cafe')
    list_filter = (
        'cafe', 'cafe__city', 'days', 'is_approved', 'is_active', 'tags',
    )
    search_fields = ('title', 'description')
    ordering = ('title',)
    filter_horizontal = ('tags', 'days')


class Request(Promo):
    """Прокси класс для вкладки Requests админ панели"""
    class Meta:
        proxy = True


class PromoRequestAdmin(PromoAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_approved=False)

    def approve(self, request, queryset):
        queryset.update(is_approved=True)

    approve.short_description = 'Approve selected requests'
    actions = ['approve']


admin.site.register(Promo, PromoAdmin)
admin.site.register(Request, PromoRequestAdmin)
