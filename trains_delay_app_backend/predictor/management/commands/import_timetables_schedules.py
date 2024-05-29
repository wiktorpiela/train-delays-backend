from django.core.management.base import BaseCommand, CommandError
from predictor.models import Route, Timetable, Station, Schedule
import csv, os

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the MyModel model.'

    def add_arguments(self, parser):
        parser.add_argument('timetable_file_path', type=str)
        parser.add_argument('schedule_file_path', type=str)

    def handle(self, *args, **kwargs):
        timetable_path = kwargs['timetable_file_path']
        schedule_path = kwargs['schedule_file_path']

        if not os.path.exists(timetable_path):
            raise CommandError(f'CSV file "{timetable_path}" does not exist')
        
        elif not os.path.exists(schedule_path):
            raise CommandError(f'CSV file "{schedule_path}" does not exist')
        
        self.import_data_from_csv(timetable_path, schedule_path)

    def import_data_from_csv(self, timetable_path, schedule_path):
        with open(timetable_path, 'r') as timetablefile:
            reader = csv.DictReader(timetablefile)

            for row in reader:
                route_id = row['route'] 
                route_obj = Route.objects.get(id=route_id)
                timetable_instance = Timetable.objects.create(route = route_obj)

                with open(schedule_path, 'r') as schedulefile:
                    subreader = csv.DictReader(schedulefile)

                    for subrow in subreader:
                        sub_route_id = subrow['route_id']

                        if sub_route_id == route_id:
                            sub_station_id = subrow['station_id']
                            arrival_time = subrow['arrival_time']
                            departure_time = subrow['departure_time']

                            station_instance = Station.objects.get(id=sub_station_id)

                            new_schedule_instance = Schedule.objects.create(
                                timetable = timetable_instance,
                                station = station_instance,
                                arrival_time = arrival_time,
                                departure_time = departure_time
                            )

                            new_schedule_instance.save()

                timetable_instance.save()