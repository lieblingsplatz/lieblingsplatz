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
                city=row["Ort"],
                district=row["Stadtteil"],
                senats_id=row["Senats-id"],
                email=row["HLinkEMail"],
                website=row["HLinkWeb"],
                kind_of_facility=row["lblEinrichtungsart"],
                agency=row["lblTraegerName"],
                kind_of_agency=row["lblTraegerart"],
                pedagogics=row["lblPaedSchwerpunkte"],
                focus=row["lblThemSchwerpunkte"],
                multilingualism=row["lblBesondereAngebote"],
                extras=row["lblMehrsprachigkeit"]
            ).save()

