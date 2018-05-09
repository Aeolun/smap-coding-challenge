# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Consumption, User
from datetime import datetime
from .services.aggregator import ConsumptionAggregator

# Create your tests here.
class AggregatorTestCase(TestCase):
    def setUp(self):
        self.timestamp = 1525853308

        user = User.objects.create(id=1000)
        Consumption.objects.create(user=user, datetime=datetime.fromtimestamp(self.timestamp), consumption=100)
        Consumption.objects.create(user=user, datetime=datetime.fromtimestamp(self.timestamp-30), consumption=80)

        user2 = User.objects.create(id=1001)
        Consumption.objects.create(user=user2, datetime=datetime.fromtimestamp(self.timestamp), consumption=120)
        Consumption.objects.create(user=user2, datetime=datetime.fromtimestamp(self.timestamp - 30), consumption=100)

    def test_aggregation_works(self):
        aggregator = ConsumptionAggregator()

        result = aggregator.Aggregate();

        self.assertEqual('["2018-05-09 08:07:58+00:00", "2018-05-09 08:08:28+00:00"]', aggregator.KeyToJSON(result, 'datetime'))
        self.assertEqual('[100.0, 120.0]', aggregator.KeyToJSON(result, 'max'))

    def test_user_aggregation_works(self):
        aggregator = ConsumptionAggregator()

        user = User.objects.get(id=1000)

        result = aggregator.AggregateUser(user)

        self.assertEqual(2, len(result))