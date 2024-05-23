from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Station, Route
from .api.serializers import RouteSerializer


class RouteView(APIView):

    def get(self, request):
        queryset = Route.objects.all()[0]
        serializer = RouteSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):

        station_name = request.data.get('station_name')

        if not station_name:
            return Response({'error': 'Station name is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            station = Station.objects.get(station_name=station_name)
        except Station.DoesNotExist:
            return Response({'error': 'Station not found'}, status=status.HTTP_404_NOT_FOUND)
        
        print(station.station_gps)

        routes = Route.objects.filter(station=station)

        print(routes)

        serializer = RouteSerializer(routes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

