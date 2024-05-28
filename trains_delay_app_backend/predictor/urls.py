from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register('stations', StationView, basename='all-stations')

urlpatterns = [
    #path('test/', RouteView.as_view(), name='routes'),
    # path('stations/<int:pk>/', StationByRouteView.as_view(), name='routes'),
    # path('', include(router.urls)),
]
