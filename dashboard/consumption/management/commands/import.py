from django.core.management.base import BaseCommand
from ...models import Area, Consumption, User, Tariff
from django.db import models
from datetime import datetime
from django.db import transaction
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str)

    help = 'import data'

    def handle(self, *args, **options):
        directory = options['directory']

        if len(User.objects.all()) > 0:
            doit = input('This will delete existing items, continue? [y|N] ')

            if doit.lower() != 'y':
                self.stdout.write("Aborted.")
                return

            User.objects.all().delete()

        imported_users = 0
        imported_consumption_items = 0

        with open(directory+'user_data.csv', 'r') as csvfile:
            user_reader = csv.DictReader(csvfile)
            for row in user_reader:
                imported_users += 1

                with transaction.atomic():
                    user = User()
                    user.id = row['id']

                    try:
                        area = Area.objects.get(name=row['area'])
                    except models.ObjectDoesNotExist:
                        area = Area()

                    area.name = row['area']
                    area.save()

                    try:
                        tariff = Tariff.objects.get(name=row['tariff'])
                    except models.ObjectDoesNotExist:
                        tariff = Tariff()

                    tariff.name = row['tariff']
                    tariff.save()

                    user.area = area
                    user.tariff = tariff

                    user.save()

                    items = 0

                    with open(directory + 'consumption/' + user.id + '.csv', 'r') as consumptionfile:
                        consumption_reader = csv.DictReader(consumptionfile)

                        consumptionarray = []
                        for consumption_row in consumption_reader:
                            imported_consumption_items += 1
                            items += 1

                            consumption = Consumption()
                            consumption.datetime = datetime.strptime(consumption_row['datetime']+'+0000', "%Y-%m-%d %H:%M:%S%z")
                            consumption.time = consumption.datetime.time()
                            consumption.dayofweek = consumption.datetime.weekday()
                            consumption.consumption = float(consumption_row['consumption'])

                            consumption.user = user

                            consumptionarray.append(consumption)

                        Consumption.objects.bulk_create(consumptionarray)

                    self.stdout.write(row['id'] + ': ' + str(items))

        self.stdout.write("Completed! Imported "+str(imported_users)+" users and "+str(imported_consumption_items)+" consumption objects")



