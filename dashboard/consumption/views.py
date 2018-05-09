# -*- coding: utf-8 -*-
from django.shortcuts import render
from .services.aggregator import ConsumptionAggregator
from .models import User

# Create your views here.


def summary(request):
    aggregator = ConsumptionAggregator()
    items = aggregator.Aggregate()

    users = User.objects.all()

    context = {
        'users': users,
        'keys': aggregator.KeyToJSON(items, 'datetime'),
        'sum': aggregator.KeyToJSON(items, 'sum'),
        'average': aggregator.KeyToJSON(items, 'avg'),
        'min': aggregator.KeyToJSON(items, 'min'),
        'max': aggregator.KeyToJSON(items, 'max')
    }

    return render(request, 'consumption/summary.html', context)


def detail(request, pk):
    aggregator = ConsumptionAggregator()

    user = User.objects.get(id=pk)

    items = aggregator.AggregateUser(user)
    weekdays = {}
    for i in range(0, 7):
        dayitems = aggregator.AggregateUserWeekday(user, i)
        weekdays[i] = {
            'time': aggregator.KeyToJSON(dayitems, 'time'),
            'average': aggregator.KeyToJSON(dayitems, 'avg')
        }

    context = {
        'account': user,
        'keys': aggregator.KeyToJSON(items, 'datetime'),
        'usage': aggregator.KeyToJSON(items, 'consumption'),
        'weekdays': weekdays
    }
    return render(request, 'consumption/detail.html', context)
