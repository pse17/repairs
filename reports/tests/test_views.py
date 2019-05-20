''' Test our views here'''
from django.urls import reverse
from django.test import TestCase
from reports.models import Tickets, Device, Court

class MissCO7ListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #court = Court(id='000001', name='Объект')
        #device = Device(name='Принтер', invent_number='0001', serial_number='00002')
        #for num in range(4):
        #    Tickets.objects.creaate(ticket='%s' % num, device=device, court=court, co7_state='n')
        Tickets.objects.creaate(ticket='100', co7_state='v')
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
        self.assertTrue(len(resp.context['tickets_list']) == 4)
