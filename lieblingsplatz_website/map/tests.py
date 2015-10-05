# coding=utf-8
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from map.models import Kita
from map.views import home_page, list_kitas

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


class HomePageTest(TestCase):

    def test_root_urlresolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(home_page, found.func)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(expected_html, response.content.decode())


class ListKitasPageTest(TestCase):

    def test_root_urlresolves_to_home_page_view(self):
        found = resolve('/list-kitas')
        self.assertEqual(list_kitas,found.func)

    def list_kitas_page_returns_correct_html(self):
        request = HttpRequest()
        response = list_kitas(request)
        expected_html = render_to_string('list_kitas.html')
        self.assertEqual(expected_html, response.content.decode())


class MapFunctionNotOverwritten(TestCase):

    def test_map(self):
        def do_stuff(a):
            return a + 10

        list1 = list(range(5))
        list2 = list(map(do_stuff, list1))
        self.assertEqual(10, list2[0])