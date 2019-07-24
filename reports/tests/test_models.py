'''Testing models'''
from django.test import TestCase
from reports.models import Court, ServiceCentre, Repair, Device, Ticket

class TestCourt(TestCase):
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

class TestServiceCentre(TestCase):
    ''' Test ServiceCentre model'''

    @classmethod
    def setUpTestData(cls):
        ServiceCentre.objects.create(name='repair All!')

    def test_name_max_length(self):
        service_centre = ServiceCentre.objects.get(id=1)
        max_length = service_centre._meta.get_field('name').max_length
        self.assertEqual(max_length, 80)

    def test_object_name(self):
        service_centre = ServiceCentre.objects.get(id=1)
        expected_object_name = service_centre.name
        self.assertEqual(expected_object_name, str(service_centre))

class TestRepair(TestCase):
    ''' Test Repair model'''

    @classmethod
    def setUpTestData(cls):
        Repair.objects.create(ticket='0001', diagnostic_card='0001', price=100.00)

    def test_tiket_max_length(self):
        repair = Repair.objects.get(id=1)
        max_length = repair._meta.get_field('ticket').max_length
        self.assertEqual(max_length, 8)

    def test_diagnostic_card_max_length(self):
        repair = Repair.objects.get(id=1)
        max_length = repair._meta.get_field('diagnostic_card').max_length
        self.assertEqual(max_length, 8)

    def test_price_max_digits(self):
        repair = Repair.objects.get(id=1)
        max_digits = repair._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 9)

    def test_object_name(self):
        repair = Repair.objects.get(id=1)
        expected_object_name = '%s %s' % (repair.diagnostic_card, repair.price)
        self.assertEqual(expected_object_name, str(repair))

class TestDevice(TestCase):
    ''' Test Device model'''

    @classmethod
    def setUpTestData(cls):
        Device.objects.create(name='Printer', invent_number='100001', serial_number='111110000')

    def test_name_max_length(self):
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_invent_number_max_length(self):
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('invent_number').max_length
        self.assertEqual(max_length, 12)

    def test_serial_number_max_length(self):
        device = Device.objects.get(id=1)
        max_length = device._meta.get_field('serial_number').max_length
        self.assertEqual(max_length, 12)

    def test_object_name(self):
        device = Device.objects.get(id=1)
        expected_object_name = '%s %s %s' % (
            device.name, device.invent_number, device.serial_number)
        self.assertEqual(expected_object_name, str(device))

class TestTicket(TestCase):
    ''' Test Ticket model'''

    @classmethod
    def setUpTestData(cls):
        Ticket.objects.create(ticket='000001', remark='It is test ticket')

    def test_tiket_max_length(self):
        Ticket = Ticket.objects.get(id=1)
        max_length = Ticket._meta.get_field('ticket').max_length
        self.assertEqual(max_length, 6)

    def test_remark_max_length(self):
        Ticket = Ticket.objects.get(id=1)
        max_length = Ticket._meta.get_field('remark').max_length
        self.assertEqual(max_length, 100)

    def test_object_name(self):
        Ticket = Ticket.objects.get(id=1)
        expected_object_name = Ticket.ticket
        self.assertEqual(expected_object_name, str(Ticket))
