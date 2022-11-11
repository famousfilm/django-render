from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('ping/', views.ping, name='ping'),
    path(
        'parking_spot_status/<str:status_id>/', 
        views.parking_spot_status, 
        name='parking_spot_status',
    ),
]
