from django.shortcuts import render
from django.views.generic import ListView
from sticker.models import Sticker

class StickerListView(ListView):
    ''' Displays stickers list '''
    model = Sticker