from django.urls import path

from . import views

urlpatterns = [
    path('', views.flight_main, name='flight-main'),
    path('search/', views.search_flight, name='search-flight'),
]
