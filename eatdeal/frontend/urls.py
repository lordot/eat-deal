from django.urls import path

from . import views

urlpatterns = [
    path('request/', views.promo_request, name='request'),
    path('', views.index, name='index')
]
