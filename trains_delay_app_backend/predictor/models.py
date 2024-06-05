from django.contrib.gis.db import models

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_gps = models.PointField(srid=4326)

    def __str__(self) -> str:
        return self.station_name
    
class Route(models.Model):
    route_name = models.CharField(max_length=500)
    route_gps = models.LineStringField(srid=4326)
    stations = models.ManyToManyField(Station, through='Schedule', related_name='routes')

    def fix_route_name(self):
        route_name = self.route_name.split('_')[0]
        return route_name
    
    def __str__(self) -> str:
        return self.route_name
    
    def get_all_station_names(self):
        unique_stations = []
        for station in self.stations.all():
            current_name = station.station_name
            if current_name not in unique_stations:
                unique_stations.append(current_name)
        return unique_stations
    
class Schedule(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='schedule_route')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='schedule_station')
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ('order',)

    def __str__(self) -> str:
        return f'{self.route.route_name} - {self.station.station_name}'
    
class RailwayData(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='railway_data_route')
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='railway_data_station')
    prev_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='railway_data_prev_station', blank=True, null=True)
    next_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='railway_data_next_station', blank=True, null=True)
    distance = models.DecimalField(decimal_places=20, max_digits=30)
    duration = models.DecimalField(decimal_places=20, max_digits=30)
    station_position = models.IntegerField()
    level_crossings_odometer = models.IntegerField()
    switches_odometer = models.IntegerField()