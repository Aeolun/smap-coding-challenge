from django.db.models import Sum, Avg, Min, Max
import json
from ..models import Consumption, User

class ConsumptionAggregator():
    def Aggregate(self):
        items = Consumption.objects.values('datetime').annotate(sum=Sum("consumption"),
                                                                avg=Avg("consumption"),
                                                                min=Min("consumption"),
                                                                max=Max("consumption"))
        return items

    def AggregateUserWeekday(self, user, weekday):
        items = Consumption.objects.filter(user=user, dayofweek=weekday).values('time').annotate(sum=Sum("consumption"),
                                                                avg=Avg("consumption"),
                                                                min=Min("consumption"),
                                                                max=Max("consumption"))
        return items

    def KeyToJSON(self, items, key):
        return json.dumps(list(items.values_list(key, flat=True)), sort_keys=True, default=str)

    def AggregateUser(self, user):
        items = Consumption.objects.filter(user=user)

        return items
