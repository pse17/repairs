'''Testing models'''
from django.test import TestCase

from reports.models import Court

class CourtTest(TestCase):
    ''' Test Court model'''

    @classmethod
    def setUpTestData(cls):
        Court.objects.create(id='00AA0001', name='Первый суд')

    def test_id_max_length(self):
        court = Court.objects.get(id='00AA0001')
        max_length = court._meta.get_field('id').max_length
        self.assertEqual(max_length, 8)

    def test_name_max_length(self):
        court = Court.objects.get(id='00AA0001')
        max_length = court._meta.get_field('name').max_length
        self.assertEqual(max_length, 80)

    def test_object_name(self):
        court = Court.objects.get(id='00AA0001')
        expected_object_name = court.name
        self.assertEqual(expected_object_name, str(court))
