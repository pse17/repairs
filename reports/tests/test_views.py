''' Test our views here'''
from django.urls import reverse
from django.test import TestCase
from reports.models import Ticket, Device, Court

class MissCO7ListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #court = Court(id='000001', name='Объект')
        #device = Device(name='Принтер', invent_number='0001', serial_number='00002')
        #for num in range(4):
        #    Ticket.objects.creaate(ticket='%s' % num, device=device, court=court, co7_state='n')
        Ticket.objects.creaate(ticket='100', co7_state='v')
        return super().setUpTestData()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/reports/miss-co7/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('miss-co7'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('miss-co7'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'reports/miss-co7.html')

    def test_lists_unverified_co7(self):
        resp = self.client.get(reverse('miss-co7'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['Ticket_list']) == 4)


class TicketUpdateView(TestCase):

    @classmethod
    def setUpTestData(cls):
        #court = Court(id='000001', name='Объект')
        #device = Device(name='Принтер', invent_number='0001', serial_number='00002')
        Ticket.objects.create(ticket='100', co7_state='v')

    def test_view_url_exsts(self):
        response = self.client.get('ticket/update/1')
        self.assertEqual(response.status_code, 200)

    def test_view_acces_by_name(self):
        response = self.client.get(reverse('ticket-update'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_template_exist(self):
        response = self.client.get(reverse('ticket-update'))
        self.assertTemplateUsed(response=response, template_name='reports/Ticket_form.html')