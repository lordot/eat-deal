from django.urls import path

from . import views

urlpatterns = [
    path('cities/', views.CityView.as_view(), name='cities'),
    path('promos/', views.PromoView.as_view(), name='promos'),
    path(
        'promos/<int:pk>/favorite/',
        views.PromoFavoriteView.as_view(),
        name='favorite'
    )
]
