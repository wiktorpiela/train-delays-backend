from django.contrib.gis.db import models

class Relation(models.Model):
    relation_name = models.CharField(max_length=10000)
    relation_gps = models.LineStringField(srid=4326)

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_gps = models.PointField(srid=4326)

class Route(models.Model):
    relation = models.ForeignKey(Relation, related_name='route_relation', on_delete=models.DO_NOTHING)
    station = models.ForeignKey(Station, related_name='route_station', on_delete=models.DO_NOTHING)
    
class TimeTable(models.Model):
    relation = models.ForeignKey(Relation, related_name='timetable_relation', on_delete=models.DO_NOTHING)
    station = models.ForeignKey(Station, related_name='timetable_station', on_delete=models.DO_NOTHING)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()