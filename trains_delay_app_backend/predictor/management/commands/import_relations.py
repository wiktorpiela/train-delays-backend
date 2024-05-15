from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from predictor.models import Relation

class Command(BaseCommand):
    help = 'Import stations from shapefile'

    def add_arguments(self, parser):
        parser.add_argument('shapefile_path', type=str, help='Path to the shapefile')

    def handle(self, *args, **kwargs):
        shapefilepath = kwargs['shapefile_path']
        
        mapping = {
            'relation_name': 'key',
            'relation_gps': 'LINESTRING',
        }

        ds = DataSource(shapefilepath)
        lm = LayerMapping(Relation, ds, mapping, transform=True)
        lm.save(verbose=True)