from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.city_list_view, name='city_list'),
]
