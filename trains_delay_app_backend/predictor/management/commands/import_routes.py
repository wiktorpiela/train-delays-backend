from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
from predictor.models import Route, Station
import csv, os

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the MyModel model.'

    def add_arguments(self, parser):
        parser.add_argument('shapefile_path', type=str, help='Path to the shapefile')
        parser.add_argument('csv_path', type=str, help='Path to the CSV file for ManyToMany relationships')

    def handle(self, *args, **kwargs):
        shapefile_path = kwargs['shapefile_path']
        csv_path = kwargs['csv_path']

        if not os.path.exists(shapefile_path):
            raise CommandError(f'Shapefile "{shapefile_path}" does not exist')

        if not os.path.exists(csv_path):
            raise CommandError(f'CSV file "{csv_path}" does not exist')
        
        self.import_routes_geometry_manytomanyfield(shapefile_path, csv_path)

        #self.import_data_from_csv(file_path)

    # def import_data_from_csv(self, file_path):
    #     with open(file_path, 'r') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             relation_id = row['relation'] 
    #             station_id = row['station']

    #             related_model1_instance = Relation.objects.get(id=relation_id)
    #             related_model2_instance = Station.objects.get(id=station_id)

    #             my_model_instance = Route(
    #                 relation=related_model1_instance,
    #                 station=related_model2_instance,
    #             )
    #             my_model_instance.save()

    def import_routes_geometry_manytomanyfield(self, shapefile_path, csv_path):

        ds = DataSource(shapefile_path)
        layer = ds[0]

        # for feature in layer:
        #     name = feature.get('route_name')
        #     geom = feature.geom.geos 

        #     route, created = Route.objects.get_or_create(route_name=name, defaults={'route_gps': geom})
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Created route: {name}'))
        #     else:
        #         route.route_gps = geom
        #         route.save()
        #         self.stdout.write(f'Updated route geometry: {name}')

        mapping = {
            'route_name': 'route_name',
            'route_gps': 'LINESTRING',
        }

        lm = LayerMapping(Route, ds, mapping, transform=True)
        lm.save(verbose=True)

        with open(csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                route_id, poi_id = row
                try:
                    route = Route.objects.get(id=route_id)
                    poi = Station.objects.get(id=poi_id)
                    route.station.add(poi)
                    self.stdout.write(self.style.SUCCESS(f'Added POI {poi_id} to route {route_id}'))
                except Route.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Route "{route_id}" does not exist'))
                except Station.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'POI with id "{poi_id}" does not exist'))

        self.stdout.write(self.style.SUCCESS('Import completed successfully'))