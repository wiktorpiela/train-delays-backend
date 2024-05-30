from rest_framework import serializers
from ..models import Station, Route, Schedule
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

    all_station_names = serializers.SerializerMethodField()
    stations = StationSerializer(many=True)

    class Meta:
        model = Route
        fields = '__all__'

    def get_all_station_names(self, obj):
        unique_stations = []
        for station in obj.stations.all():
            current_name = station.station_name
            if current_name not in unique_stations:
                unique_stations.append(current_name)
        return unique_stations
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fixed_field_value = representation['route_name']
        if fixed_field_value:
            representation['route_name'] = fixed_field_value.split('_')[0]
        return representation


    
