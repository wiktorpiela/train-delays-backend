from django.core.management.base import BaseCommand, CommandError
from predictor.models import Route, Timetable, Station, Schedule
from predictor.utils.import_data_utils import filter_csv_dict
import csv, os

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the MyModel model.'

    def add_arguments(self, parser):
        parser.add_argument('schedule_file_path', type=str)

    def handle(self, *args, **kwargs):
        schedule_path = kwargs['schedule_file_path']
        
        if not os.path.exists(schedule_path):
            raise CommandError(f'CSV file "{schedule_path}" does not exist')
        
        self.import_data_from_csv(schedule_path)

    def import_data_from_csv(self, schedule_path):
        routes = Route.objects.all()

        for route in routes:
            timetable_instance = Timetable.objects.create(route=route)

            filter_criteria = {'route_id': str(route.id)}
            with open(schedule_path, 'r') as schedulefile:
                reader = csv.DictReader(schedulefile)
            
                rows = filter_csv_dict(reader, filter_criteria)
                for row in rows:
                    sub_station_id = row['station_id']
                    arrival_time = row['arrival_time']
                    departure_time = row['departure_time']

                    station_instance = Station.objects.get(id=sub_station_id)

                    new_schedule_instance = Schedule.objects.create(
                        timetable = timetable_instance,
                        station = station_instance,
                        arrival_time = arrival_time,
                        departure_time = departure_time
                    )

                    new_schedule_instance.save()

            timetable_instance.save()