'''Testing models'''
from django.test import TestCase
from reports.models import Court, Repair, Ticket

class TestCourt(TestCase):
    ''' Test Court model'''

    @classmethod
    def setUpTestData(cls):
        Court.objects.create(id='00AA0001', name='Первый суд')

    def setUp(self):
        self.court = Court.objects.get(id='00AA0001')

    def test_id_max_length(self):
        max_length = self.court._meta.get_field('id').max_length
        self.assertEqual(max_length, 8)

    def test_name_max_length(self):
        max_length = self.court._meta.get_field('name').max_length
        self.assertEqual(max_length, 80)

    def test_object_name(self):
        expected_name = self.court.name
        self.assertEqual(expected_name, str(self.court))


class TestRepair(TestCase):
    ''' Test Repair model'''

    @classmethod
    def setUpTestData(cls):
        Repair.objects.create(ticket='0001', diagnostic_card='0001', price=100.00)

    def setUp(self):
        self.repair = Repair.objects.get(id=1)

    def test_diagnostic_card_max_length(self):
        max_length = self.repair._meta.get_field('diagnostic_card').max_length
        self.assertEqual(max_length, 8)

    def test_price_max_digits(self):
        max_digits = self.repair._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 9)

    def test_object_name(self):
        expected_object_name = '%s %s' % (self.repair.diagnostic_card, self.repair.price)
        self.assertEqual(expected_object_name, str(self.repair))


class TestTicket(TestCase):
    ''' Test Ticket model'''

    @classmethod
    def setUpTestData(cls):
        Ticket.objects.create(ticket='000001', remark='It is test ticket')
    
    def setUp(self):
        self.ticket = Ticket.objects.get(id=1)

    def test_tiket_max_length(self):
        max_length = self.ticket._meta.get_field('ticket').max_length
        self.assertEqual(max_length, 6)

    def test_name_max_length(self):
        max_length = self.ticket._meta.get_field('name').max_length
        self.assertEqual(max_length, 80)

    def test_invent_number_max_length(self):
        max_length = self.ticket._meta.get_field('invent_number').max_length
        self.assertEqual(max_length, 18)

    def test_serial_number_max_length(self):
        max_length = self.ticket._meta.get_field('serial_number').max_length
        self.assertEqual(max_length, 24)
    
    def test_object_name(self):
        expected_name = '000001'
        self.assertEqual(expected_name, str(self.ticket))
