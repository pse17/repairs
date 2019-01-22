from django.test import TestCase
from sticker.forms import StickerForm

class TestStickerForm(TestCase):

    def setUp(self):
        self.form = StickerForm()
        return super().setUp()

    def test_invent_number_field(self):
        self.assertEqual(self.form.fields['invent_number'].label, 'Инвентарный № :')
