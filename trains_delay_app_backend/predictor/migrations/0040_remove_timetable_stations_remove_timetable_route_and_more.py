# Generated by Django 5.0.6 on 2024-05-29 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0039_route_schedule_timetable_schedule_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='stations',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='route',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
    ]
