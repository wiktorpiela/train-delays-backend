# Generated by Django 5.0.6 on 2024-05-12 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0007_remove_station_station_gps'),
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
