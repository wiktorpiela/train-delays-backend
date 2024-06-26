# Generated by Django 5.0.6 on 2024-05-16 15:47

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('predictor', '0012_remove_timetable_relation_remove_route_relation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=100)),
                ('station_gps', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=10000)),
                ('route_gps', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='station_route', to='predictor.station')),
            ],
        ),
    ]
