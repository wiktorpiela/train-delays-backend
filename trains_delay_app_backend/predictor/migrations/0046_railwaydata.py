# Generated by Django 5.0.6 on 2024-06-05 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0045_route_schedule_route_stations'),
    ]

    operations = [
        migrations.CreateModel(
            name='RailwayData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=1, max_digits=10)),
                ('duration', models.DecimalField(decimal_places=1, max_digits=10)),
                ('station_position', models.IntegerField()),
                ('level_crossings_odometer', models.IntegerField()),
                ('switches_odometer', models.IntegerField()),
                ('next_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='railway_data_next_station', to='predictor.station')),
                ('prev_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='railway_data_prev_station', to='predictor.station')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='railway_data_route', to='predictor.route')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='railway_data_station', to='predictor.station')),
            ],
        ),
    ]
