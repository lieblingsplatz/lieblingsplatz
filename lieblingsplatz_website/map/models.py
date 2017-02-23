from django.db import models


class Kita(models.Model):
    name = models.TextField()
    # address
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    zip_code = models.IntegerField()
    city = models.TextField()
    district = models.TextField() # better: define choices als field option!
    senats_id = models.IntegerField()
    # phone (many-to-one!)
    #phonenumber = models.
    # email (many-to-one! later maybe) website
    email = models.EmailField()
    website = models.URLField()
    # orga-info
    kind_of_facility = models.TextField() #einrichtungsart
    agency = models.TextField() #traeger
    kind_of_agency = models.TextField() #traegerart
    # pedagogics
    # lblPaedAnsaetze -> in Helens Liste nicht vorhanden
    pedagogics = models.TextField() # lblPaedSchwerpunkte
    focus = models.TextField() # lblThemSchwerpunkte
    multilingualism = models.TextField() # lblMehrsprachigkeit
    extras = models.TextField() # lblBesondereAngebote
    # opening hours
    # numbers, ages, structure
 