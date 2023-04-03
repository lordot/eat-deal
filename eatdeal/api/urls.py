from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.city_list_view, name='city_list'),
    path('promos/', views.PromoViewSet.as_view({'get': 'list'}), name='promos')
]
