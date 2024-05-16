from django.core.management.base import BaseCommand
from predictor.models import Route, Station, Relation
import csv

class Command(BaseCommand):
    help = 'Imports data from a CSV file into the MyModel model.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        file_path = options['file_path']
        self.import_data_from_csv(file_path)

    def import_data_from_csv(self, file_path):
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                relation_id = row['relation'] 
                station_id = row['station']

                related_model1_instance = Relation.objects.get(id=relation_id)
                related_model2_instance = Station.objects.get(id=station_id)

                my_model_instance = Route(
                    relation=related_model1_instance,
                    station=related_model2_instance,
                )
                my_model_instance.save()