from django.core.management.base import BaseCommand, CommandError
from predictor.models import RailwayData, Route, Station
import os, csv
from predictor.utils.import_data_utils import get_or_none

class Command(BaseCommand):
    help = 'Import railway data to prediction from csv'

    def add_arguments(self, parser):
        parser.add_argument('csvfile_path', type=str, help='Path to the csv file')

    def handle(self, *args, **kwargs):
        csvfilepath = kwargs['csvfile_path']

        if not os.path.exists(csvfilepath):
            raise CommandError(f'CSV file "{csvfilepath}" does not exist')

        self.import_railway_data_from_csv(csvfilepath)

    def import_railway_data_from_csv(self, csvfilepath):

        with open(csvfilepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                route = Route.objects.get(id=row['pk_route'])
                station = Station.objects.get(id=row['pk_station_current'])

                prev_station = get_or_none(Station, id=row['pk_station_prev'])
                next_station = get_or_none(Station, id=row['pk_station_next'])

                distance = row['distances']
                duration = row['durations']
                stations_count = row['stations_count']
                level_crossing_count = row['level_crossing_count']
                switches_count = row['switches_count']

                RailwayData.objects.create(
                    route = route,
                    station = station,
                    prev_station = prev_station,
                    next_station = next_station,
                    distance = distance,
                    duration = duration,
                    station_position = stations_count,
                    level_crossings_odometer = level_crossing_count,
                    switches_odometer = switches_count
                )