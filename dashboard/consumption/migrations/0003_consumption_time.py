# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0002_consumption_dayofweek'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumption',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]