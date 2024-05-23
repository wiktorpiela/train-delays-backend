from rest_framework import serializers
from ..models import Station, Route, Timetable
from django.contrib.gis.geos import Point
from .fields import UniqueListField

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('station_name',)

class TimetableSerializer(serializers.ModelSerializer):
    station = serializers.StringRelatedField()
    station_gps = serializers.SerializerMethodField()

    class Meta:
        model = Timetable
        fields = ('id', 'station', 'arrival_time', 'departure_time', 'station_gps')

    def get_station_gps(self, obj):
        return {
            'lat': obj.station.station_gps.y,
            'lon': obj.station.station_gps.x,
            }

class RouteSerializer(serializers.ModelSerializer):
    timetable_relation = TimetableSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'route_name', 'timetable_relation', 'route_gps')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['route_name'] = instance.route_name.split('_')[0]
        return representation