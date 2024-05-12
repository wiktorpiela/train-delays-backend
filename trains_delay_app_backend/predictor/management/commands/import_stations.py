from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from predictor.models import Station

class Command(BaseCommand):
    help = 'Import stations from shapefile'

    def handle(self, *args, **kwargs):
        mapping = {
            'station_name': 'Stacja',
            'station_gps': 'POINT',
        }

        # Path to your shapefile
        shapefile = '/path/to/your/stations_gps.shp'

        # Mapping the shapefile fields to the model fields
        lm = LayerMapping(Station, shapefile, mapping)
        lm.save(verbose=True)
