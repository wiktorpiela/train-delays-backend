from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from predictor.models import Station

class Command(BaseCommand):
    help = 'Import stations from shapefile'

    def add_arguments(self, parser):
        parser.add_argument('shapefile_path', type=str, help='Path to the shapefile')

    def handle(self, *args, **kwargs):
        shapefilepath = kwargs['shapefile_path']
        mapping = {
            'station_name': 'Stacja',
            'station_gps': 'POINT',
        }

        ds = DataSource(shapefilepath)
        layer = ds[0]
        print(layer.fields)
        print(len(layer))  
        print(layer.geom_type)  
        print(layer.srs)

        lm = LayerMapping(Station, ds, mapping, transform=True)
        lm.save(verbose=True)
