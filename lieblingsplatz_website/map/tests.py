# coding=utf-8
from django.test import TestCase
from map.models import Kita

class ModelTests(TestCase):
    def test_kita_model(self):
        first_kita = Kita()
        first_kita.name = u'Kita 1'
        first_kita.latitude = 1234.5678
        first_kita.longitude = -1234.5678
        first_kita.address = u'Berliner Bärenweg 23'
        first_kita.district = u'Kreuzberg'
        first_kita.zip_code = 10825
        first_kita.senats_id = 2342
        first_kita.save()
        
        second_kita = Kita()
        second_kita.name = u'Kita 2'
        second_kita.latitude = -908.5678
        second_kita.longitude = -0.5678
        second_kita.address = u'Wassermelonenallee 42'
        second_kita.district = u'Schöneberg'
        second_kita.zip_code = 14482
        second_kita.senats_id = 1337
        second_kita.save()

        kitas = Kita.objects.all()
        self.assertEqual(kitas.count(), 2)
        saved_first_kita = kitas[0]

        self.assertEqual(saved_first_kita.name, u'Kita 1')
        self.assertEqual(saved_first_kita.latitude, 1234.5678)
        self.assertEqual(saved_first_kita.longitude, -1234.5678)
        self.assertEqual(saved_first_kita.address, u'Berliner Bärenweg 23')
        self.assertEqual(saved_first_kita.district, u'Kreuzberg')
        self.assertEqual(saved_first_kita.zip_code, 10825)
        self.assertEqual(saved_first_kita.senats_id, 2342)