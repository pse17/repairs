from django.test import TestCase
from django.urls import reverse
from sticker.models import Sticker

class StickerListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for stiker_num in range(3):
            pass