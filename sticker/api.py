import logging
from rest_framework import generics
from sticker.models import Sticker
from sticker.serializers import *

logger = logging.getLogger(__name__)


class StickerAdd(generics.CreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer


class StickerUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer


class StickerList(generics.ListAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer


class CourtList(generics.ListAPIView):
	queryset = CourtForSticker.objects.all()
	serializer_class = CourtSerializer