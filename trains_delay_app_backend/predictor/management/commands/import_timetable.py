from django.core.management.base import BaseCommand
from predictor.models import Timetable, Station, Route
import csv

class Command(BaseCommand):
    help = 'Import stations from shapefile'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help='Path to the csv file')

    def handle(self, *args, **kwargs):
        csvfilepath = kwargs['csv_path']
        self.import_csv_into_timetable_model(csvfilepath)

    def import_csv_into_timetable_model(self, file_path):
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                foreign_key1_id = row['route']
                foreign_key2_id = row['station']

                route_instance = Route.objects.get(id=foreign_key1_id)
                station_instance = Station.objects.get(id=foreign_key2_id)

                timetable_instance = Timetable.objects.create(
                    route=route_instance,
                    station=station_instance,
                    arrival_time = row['arrival_time']
                    departure_time = row['departure_time']
                )

                timetable_instance.save()