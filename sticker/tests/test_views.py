from django.test import TestCase
from django.urls import reverse
from sticker.models import Sticker

class StickerListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for stiker_num in range(3):
            Sticker.objects.create(device_name='Принтер %s' % stiker_num,\
                invent_number='00000%s' % stiker_num)

    def test_view_list_url(self):
        resp = self.client.get('/sticker/list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_list_by_name(self):
        resp = self.client.get(reverse('sticker_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_create_tmplate(self):
        resp = self.client.get(reverse('sticker_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='sticker/sticker_create.html')

    def test_view_update_tmplate(self):
        resp = self.client.get(reverse('sticker_update', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='sticker/sticker_update.html')