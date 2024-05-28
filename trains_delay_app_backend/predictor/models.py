from django.contrib.gis.db import models

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_gps = models.PointField(srid=4326)

    def __str__(self) -> str:
        return self.station_name
    
class Route(models.Model):
    route_name = models.CharField(max_length=500)
    route_gps = models.LineStringField(srid=4326)

    def fix_route_name(self):
        route_name = self.route_name.split('_')[0]
        return route_name
    
    def __str__(self) -> str:
        return self.route_name
    
class Timetable(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='timetables')
    stations = models.ManyToManyField(Station, through='Schedule', related_name='timetables')

    def __str__(self) -> str:
        return f'{self.route.route_name} - {self.stations.station_name}'

class Schedule(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='schedules')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='schedules')
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
