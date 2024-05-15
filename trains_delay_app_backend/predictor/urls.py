from django.urls import path
from .views import *

urlpatterns = [
    path('stations/', StationView.as_view(), name='stations'),
    path('relations/<int:pk>/', RelationView.as_view(), name='relations'),
]
