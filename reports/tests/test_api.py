''' Test API '''
import json
from django.test import TestCase
from django.urls import reverse
from reports.models import Ticket, Court

class TestTicketListAPI(TestCase):
    ''' Test Ticket list API '''
    @classmethod
    def setUpTestData(cls):
        court = Court.objects.create(id='00AA0001', name='Высокий суд')
        Ticket.objects.create(ticket='000001', court=court, name='Принтер', invent_number='00001', serial_number='00A-01')
        Ticket.objects.create(ticket='000002', court=court, name='Монитор', invent_number='00002', serial_number='00A-02')

    def test_list(self):
        list_url = reverse('list_ticket')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '000001')
        self.assertContains(response, '000002')


class TestTicketAPI(TestCase):
    ''' Test Ticket detail/update API '''

    @classmethod
    def setUpTestData(cls):
        court = Court.objects.create(id='00AA0001', name='Высокий суд')
        Ticket.objects.create(ticket='000001', court=court, name='Принтер', invent_number='00001', serial_number='00A-01')

    def test_detail(self):
        detail_update_url = reverse('detail_update_ticket', kwargs={'pk': 1})
        response = self.client.get(detail_update_url)
        self.assertEqual(response.status_code, 200)

        test_content = {'ticket': '000001', 'court': {'id': '00AA0001', 'name': 'Высокий суд'},
            'name': 'Принтер', 'invent_number': '00001', 'serial_number': '00A-01'}
        data = json.loads(response.content)
        self.assertEqual(data, test_content)


    def test_update(self):
        detail_update_url = reverse('detail_update_ticket', kwargs={'pk': 1})
        put = json.dumps({'ticket': '000001', 'court': {'id': '00AA0001', 'name': 'Высокий суд'},
            'name': 'Принтер', 'invent_number': '00001', 'serial_number': '00B-01'})
        
        response = self.client.put(detail_update_url, put, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '00B-01')
        
