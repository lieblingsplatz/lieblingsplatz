from django.db import models


class Kita(models.Model):
    name = models.CharField(max_length=255)
    # address
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255) # better: define choices als field option!
    senats_id = models.IntegerField()
    # email (many-to-one! later maybe) website
    phonenumber = models.CharField(max_length=31)
    email = models.CharField(max_length=255) # EmailField()
    website = models.URLField()
    # orga-info
    kind_of_facility = models.CharField(max_length=255) #einrichtungsart
    agency = models.CharField(max_length=255) #traeger
    kind_of_agency = models.CharField(max_length=255) #traegerart
    # pedagogics
    # lblPaedAnsaetze -> in Helens Liste nicht vorhanden
    pedagogics = models.TextField() # lblPaedSchwerpunkte
    focus = models.TextField() # lblThemSchwerpunkte
    multilingualism = models.TextField() # lblMehrsprachigkeit
    extras = models.TextField() # lblBesondereAngebote
    # opening hours
    # numbers, ages, structure

    def __str__(self):
        return self.name

class Phone(models.Model):
    kita = models.ForeignKey(Kita, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=31)

    def __str__(self):
        return self.phonenumber
 