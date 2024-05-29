from rest_framework import serializers
from ..models import Station, Route
from django.contrib.gis.geos import Point

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'station_name', 'station_gps',)

class RouteSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    stations = serializers.SerializerMethodField()

    class Meta:
        model = Route
        fields = '__all__'

    def get_stations(self, obj):
        unique_stations = []
        for station in obj.stations.all():
            current_name = station.station_name
            if current_name not in unique_stations:
                unique_stations.append(current_name)
        return unique_stations


    
