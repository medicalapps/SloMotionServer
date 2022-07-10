# Generated by Django 3.1.2 on 2022-07-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0004_gpswaypoint_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpswaypoint',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gpswaypoint',
            name='order',
            field=models.IntegerField(blank=True, default=-1),
        ),
    ]
