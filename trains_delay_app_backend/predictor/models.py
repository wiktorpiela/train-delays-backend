from django.contrib.gis.db import models

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_gps = models.PointField(srid=4326)

    def __str__(self) -> str:
        return self.station_name

class Route(models.Model):
    route_name = models.CharField(max_length=500)
    route_gps = models.LineStringField(srid=4326)
    station = models.ManyToManyField(Station, related_name='route') #stations #routes

    def fix_relation_name(self):
        rel_name = self.relation_name.split('_')[0]
        return rel_name
    
    def __str__(self) -> str:
        return self.route_name

class Timetable(models.Model):
    route = models.ForeignKey(Route, related_name='timetable_relation', on_delete=models.DO_NOTHING)
    station = models.ForeignKey(Station, related_name='timetable_station', on_delete=models.DO_NOTHING)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self) -> str:
        return f'{self.route.route_name} - {self.station.station_name} - {self.arrival_time}'