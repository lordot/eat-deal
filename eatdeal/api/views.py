from django.http import JsonResponse

from .models import City


def city_list_view(request):
    cities = City.objects.all().values('name')
    return JsonResponse(list(cities), safe=False)
