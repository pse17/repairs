'''Testing model'''

from django.test import TestCase
from sticker.models import Sticker
from reports.models import Court

class StickerTest(TestCase):
    ''' Test Sticker model'''

    @classmethod
    def setUpTestData(cls):
        Court.objects.create(id='00AA0001', name='Первый суд')
        court = Court.objects.get(id='00AA0001')
        Sticker.objects.create(court=court, device_name='Принтер', invent_number='0001',\
            serial_number='0002', production_date=2017, malfunction='Сломался')

    def setUp(self):
        self.sticker = Sticker.objects.get(id=1)

    def test_court(self):
        court_name = self.sticker.court.name
        self.assertEqual(court_name, 'Первый суд')

    def test_device_name(self):
        max_length = self.sticker._meta.get_field('device_name').max_length
        blank = self.sticker._meta.get_field('device_name').null
        self.assertEqual(max_length, 80)
        self.assertFalse(blank)

    def test_invent_number(self):
        max_length = self.sticker._meta.get_field('invent_number').max_length
        blank = self.sticker._meta.get_field('invent_number').null
        self.assertEqual(max_length, 18)
        self.assertFalse(blank)

    def test_serial_number(self):
        max_length = self.sticker._meta.get_field('serial_number').max_length
        self.assertEqual(max_length, 24)
        blank = self.sticker._meta.get_field('serial_number').blank
        self.assertTrue(blank)

    def test_production_date(self):
        max_length = self.sticker._meta.get_field('production_date').max_length
        self.assertEqual(max_length, 4)
        blank = self.sticker._meta.get_field('production_date').blank
        self.assertTrue(blank)

    def test_malfunctione(self):
        blank = self.sticker._meta.get_field('malfunction').blank
        self.assertTrue(blank)