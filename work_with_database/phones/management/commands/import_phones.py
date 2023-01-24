import csv

from django.core.management.base import BaseCommand
from django.http import HttpResponse

from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for row in phones:
                Phone.objects.create(id=row[0], name=row[1],  image=row[2],price=row[3], release_date=row[4], lte_exists=row[5], slug=row[6])
                Phone.save(*args, **options)

