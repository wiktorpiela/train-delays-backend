from django.urls import path
from .views import *

urlpatterns = [
    path('test/', RouteView.as_view(), name='routes'),
]
