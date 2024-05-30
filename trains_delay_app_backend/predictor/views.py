from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

from .models import Station, Route
from .api.serializers import StationSerializer, RouteSerializer

from .utils.locked_stations import LOCKED_STATIONS

class StationView(viewsets.ReadOnlyModelViewSet):
    serializer_class = StationSerializer

    def get_queryset(self):
        ids_to_exclude = [item[0] for item in LOCKED_STATIONS]
        queryset = Station.objects.exclude(id__in=ids_to_exclude)
        return queryset
       
class StationByRouteView(APIView):

    def get(self, request, pk):
        start_station = Station.objects.get(id=pk)
        routes = Route.objects.filter(stations=start_station)

        unique_stations = []
        for route in routes:
            current_route_stations = route.get_all_station_names()
            unique_stations.append(current_route_stations)
        unique_stations = list(set([item for sublist in unique_stations for item in sublist]))

        serializer = RouteSerializer(routes, many=True, fields=('route_name', 'all_station_names',))

        # return Response({'stations': sorted(unique_stations)})
        return Response(serializer.data)
    

    

