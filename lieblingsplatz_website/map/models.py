from django.db import models


class Kita(models.Model):
    name = models.CharField(max_length=255)
    # address
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    extra_address_line = models.CharField(max_length=255, blank=True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255, default='Berlin')
    district = models.CharField(max_length=255) # better: define choices als field option!
    senats_id = models.IntegerField(default=0)
    phonenumber = models.CharField(max_length=255, blank=True)
    # email (many-to-one! later maybe) website
    email = models.CharField(max_length=255, blank=True) # EmailField()
    website = models.URLField(blank=True)
    # orga-info
    kind_of_facility = models.CharField(max_length=255, blank=True) #einrichtungsart
    agency = models.CharField(max_length=255, blank=True) #traeger
    kind_of_agency = models.CharField(max_length=255, blank=True) #traegerart
    # pedagogics
    # lblPaedAnsaetze -> in Helens Liste nicht vorhanden
    pedagogics = models.TextField(blank=True) # lblPaedSchwerpunkte
    focus = models.TextField(blank=True) # lblThemSchwerpunkte
    multilingualism = models.TextField(blank=True) # lblMehrsprachigkeit
    extras = models.TextField(blank=True) # lblBesondereAngebote
    # opening hours
    monday_open = models.CharField(max_length=31, blank=True)
    monday_close = models.CharField(max_length=31, blank=True)
    tuesday_open = models.CharField(max_length=31, blank=True)
    tuesday_close = models.CharField(max_length=31, blank=True)
    wednesday_open = models.CharField(max_length=31, blank=True)
    wednesday_close = models.CharField(max_length=31, blank=True)
    thursday_open = models.CharField(max_length=31, blank=True)
    thursday_close = models.CharField(max_length=31, blank=True)
    friday_open = models.CharField(max_length=31, blank=True)
    friday_close = models.CharField(max_length=31, blank=True)
    saturday_open = models.CharField(max_length=31, blank=True)
    saturday_close = models.CharField(max_length=31, blank=True)
    sunday_open = models.CharField(max_length=31, blank=True)
    sunday_close = models.CharField(max_length=31, blank=True)
    # numbers, ages, structure

    def __str__(self):
        return self.name

class Phone(models.Model):
    kita = models.ForeignKey(Kita, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=31)

    def __str__(self):
        return self.phonenumber
 