from rest_framework import generics, status, viewsets
from rest_framework.views import APIView

from rest_framework.response import Response
from .models import Station, Route, Timetable
from .api.serializers import RouteSerializer, StationSerializer, TimetableSerializer

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
        routes = Route.objects.filter(station=start_station)
        routes = RouteSerializer(routes, many=True)
        return Response({'hello':routes.data})


# class RouteView(APIView):

#     def get(self, request):
#         queryset = Route.objects.all()[0]
#         serializer = RouteSerializer(queryset)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request, format=None):

#         station_name = request.data.get('station_name')

#         if not station_name:
#             return Response({'error': 'Station name is required'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             station = Station.objects.get(station_name=station_name)
#         except Station.DoesNotExist:
#             return Response({'error': 'Station not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         print(station.station_gps)

#         routes = Route.objects.filter(station=station)

#         print(routes)

#         serializer = RouteSerializer(routes, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)

