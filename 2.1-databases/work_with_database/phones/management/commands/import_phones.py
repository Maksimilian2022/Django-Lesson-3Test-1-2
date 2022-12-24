import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            i = 0
            new_phone = Phone(name=phone['name'], img=phone['image'], price='NONE', release_data='NONE', lte_exist=phone['lte_exists'], slug='NONE')
            new_phone.save()
            i += 1

