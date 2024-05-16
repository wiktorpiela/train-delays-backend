# Generated by Django 5.0.6 on 2024-05-16 04:53

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0010_remove_timetable_station_remove_timetable_relation_and_more'),
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
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='route_relation', to='predictor.relation')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='route_station', to='predictor.station')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='timetable_relation', to='predictor.relation')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='timetable_station', to='predictor.station')),
            ],
        ),
    ]
