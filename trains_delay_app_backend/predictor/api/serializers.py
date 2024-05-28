from rest_framework import serializers
# from ..models import Station, Route, Timetable
# from django.contrib.gis.geos import Point

# class StationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Station
#         fields = ('id', 'station_name', 'station_gps',)

# class TimetableSerializer(serializers.ModelSerializer):
#     station = serializers.StringRelatedField()
#     station_gps = serializers.SerializerMethodField()

#     class Meta:
#         model = Timetable
#         fields = ('id', 'station', 'arrival_time', 'departure_time', 'station_gps')

#     def get_station_gps(self, obj):
#         return {
#             'lat': obj.station.station_gps.y,
#             'lon': obj.station.station_gps.x,
#             }

# class RouteSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         fields = kwargs.pop('fields', None)
#         super().__init__(*args, **kwargs)

#         if fields is not None:
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)

#     timetable_relation = TimetableSerializer(many=True)

#     class Meta:
#         model = Route
#         fields = ('id', 'route_name', 'timetable_relation', 'route_gps')

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['route_name'] = instance.route_name.split('_')[0]
#         return representation