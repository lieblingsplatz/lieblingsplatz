__author__ = 'ellen'

import os
import csv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lieblingsplatz_website.settings")

application = get_wsgi_application()

from map.models import Kita


def import_csv_into_db(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            Kita(
                name=row["lblKitaname"],
                latitude=float(row["lat"]),
                longitude=float(row["lon"]),
                address=row["lblStrasse"],
                zip_code=row["PLZ"],
                district=row["Stadtteil"],
                senats_id=row["Senats-id"]
            ).save()

