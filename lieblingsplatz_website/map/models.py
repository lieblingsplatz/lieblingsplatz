from django.db import models


class Kita(models.Model):
    name = models.CharField(max_length=255)
    # address
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255, default='Berlin')
    district = models.CharField(max_length=255) # better: define choices als field option!
    senats_id = models.IntegerField(default=0)
    phonenumber = models.CharField(max_length=255, default='')
    # email (many-to-one! later maybe) website
    email = models.CharField(max_length=255, default='') # EmailField()
    website = models.URLField(default='')
    # orga-info
    kind_of_facility = models.CharField(max_length=255, default='') #einrichtungsart
    agency = models.CharField(max_length=255, default='') #traeger
    kind_of_agency = models.CharField(max_length=255, default='') #traegerart
    # pedagogics
    # lblPaedAnsaetze -> in Helens Liste nicht vorhanden
    pedagogics = models.TextField(default='') # lblPaedSchwerpunkte
    focus = models.TextField(default='') # lblThemSchwerpunkte
    multilingualism = models.TextField(default='') # lblMehrsprachigkeit
    extras = models.TextField(default='') # lblBesondereAngebote
    # opening hours
    monday_open = models.CharField(max_length=31, default='')
    monday_close = models.CharField(max_length=31, default='')
    tuesday_open = models.CharField(max_length=31, default='')
    tuesday_close = models.CharField(max_length=31, default='')
    wednesday_open = models.CharField(max_length=31, default='')
    wednesday_close = models.CharField(max_length=31, default='')
    thursday_open = models.CharField(max_length=31, default='')
    thursday_close = models.CharField(max_length=31, default='')
    friday_open = models.CharField(max_length=31, default='')
    friday_close = models.CharField(max_length=31, default='')
    saturday_open = models.CharField(max_length=31, default='')
    saturday_close = models.CharField(max_length=31, default='')
    sunday_open = models.CharField(max_length=31, default='')
    sunday_close = models.CharField(max_length=31, default='')
    # numbers, ages, structure

    def __str__(self):
        return self.name

class Phone(models.Model):
    kita = models.ForeignKey(Kita, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=31)

    def __str__(self):
        return self.phonenumber
 