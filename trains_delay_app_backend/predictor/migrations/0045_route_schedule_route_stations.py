# Generated by Django 5.0.6 on 2024-05-29 14:43

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0044_remove_timetable_route_remove_schedule_station_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=500)),
                ('route_gps', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_route', to='predictor.route')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_station', to='predictor.station')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='route',
            name='stations',
            field=models.ManyToManyField(related_name='routes', through='predictor.Schedule', to='predictor.station'),
        ),
    ]
