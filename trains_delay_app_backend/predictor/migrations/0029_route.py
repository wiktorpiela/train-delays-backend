# Generated by Django 5.0.6 on 2024-05-21 06:59

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0028_delete_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=500)),
                ('route_gps', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('station', models.ManyToManyField(related_name='route', to='predictor.station')),
            ],
        ),
    ]