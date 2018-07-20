from django.urls import path

from . import views

urlpatterns = [
    path('', views.flight_main, name='flight-main'),
    path('search/<str:origin>/<str:destination>/<int:month>', views.search_flight, name='search-flight'),
    path('<int:pk>/', views.flight_detail, name='flight-detail'),
]
