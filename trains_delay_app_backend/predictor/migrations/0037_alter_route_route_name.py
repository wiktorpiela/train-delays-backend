# Generated by Django 5.0.6 on 2024-05-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0036_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_name',
            field=models.CharField(max_length=500),
        ),
    ]
