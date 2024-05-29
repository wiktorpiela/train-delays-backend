from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

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

        # wektoryzacja na np array ------
        stations_b = []
        for route in routes:
            stations = route.stations.all()
            for station in stations:
                current_name = station.station_name
                if current_name not in stations_b:
                    stations_b.append(current_name)

        route_names_list = []
        stations = []
        
        # ['Węgliniec - Wrocław Główny', 'sadasd', 'asdasd']
        # [['a', 'b', 'c', 'd'], ['x','y','z'], [],]
        for route in routes:
            print(f"{route.route_name.split('_')[0]} ------------- ")
            all_stations = route.stations.all()
            for station in all_stations:
                print(station.station_name)

        serializer = RouteSerializer(routes, many=True, fields=('route_name','stations',))
        return Response(serializer.data)
        # return Response({'stations': sorted(stations_b)
                         
                         
        #                  }, 
                        #  'routes': [
                        #      {
                        #          'route_name': 'Węgliniec - Wrocław Główny',
                        #          'route_stations': ['Wrocław Główny', 'Malczyce', ....]
                        #      },
                        #      {
                        #         'route_name': 'Węgliniec - Wrocław Główny',
                        #         'route_stations': ['Wrocław Główny', 'Malczyce', ....]
                        #      }
                        #  ]
                        #  }

    

