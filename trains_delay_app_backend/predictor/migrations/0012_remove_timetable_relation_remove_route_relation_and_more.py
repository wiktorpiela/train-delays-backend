# Generated by Django 5.0.6 on 2024-05-16 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0011_station_route_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='route',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='route',
            name='station',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='station',
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Station',
        ),
        migrations.DeleteModel(
            name='TimeTable',
        ),
    ]