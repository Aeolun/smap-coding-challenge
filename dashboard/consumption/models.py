# -*- coding: utf-8 -*-
from django.db import models

class Area(models.Model):
    name = models.TextField()

class Tariff(models.Model):
    name = models.TextField()

# Create your models here.
class User(models.Model):
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True)

class Consumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    datetime = models.DateTimeField()
    dayofweek = models.IntegerField(null=True)
    time = models.TimeField(null=True)
    consumption = models.FloatField()