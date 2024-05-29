from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from predictor.models import Route, Station, Schedule
import os, csv

class Command(BaseCommand):
    help = 'Import stations from shapefile'

    def add_arguments(self, parser):
        parser.add_argument('shapefile_path', type=str, help='Path to the shapefile')
        parser.add_argument('csvfile_path', type=str, help='Path to the csv file')

    def handle(self, *args, **kwargs):
        shapefilepath = kwargs['shapefile_path']
        csvfilepath = kwargs['csvfile_path']

        if not os.path.exists(shapefilepath):
            raise CommandError(f'Shapefile "{shapefilepath}" does not exist')
        
        elif not os.path.exists(csvfilepath):
            raise CommandError(f'CSV file "{csvfilepath}" does not exist')

        self.import_routes_schedules_data(shapefilepath, csvfilepath)


    def import_routes_schedules_data(self, shapefilepath, csvfilepath):
        mapping = {
            'route_name': 'route_name',
            'route_gps': 'LINESTRING',
        }

        ds = DataSource(shapefilepath)
        lm = LayerMapping(Route, ds, mapping, transform=True)
        lm.save(verbose=True)

        with open(csvfilepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                route_obj = Route.objects.get(id=row['route'])
                station_obj = Station.objects.get(id=row['station'])

                schedule_obj = Schedule.objects.create(
                    route = route_obj,
                    station = station_obj,
                    order = row['order']
                )

                schedule_obj.save()