# Generated by Django 4.1 on 2022-08-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_origin_trip_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
