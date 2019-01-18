from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from sticker.models import Sticker

class StickerListView(ListView):
    ''' Displays stickers list '''
    model = Sticker

class StickerCreateView(CreateView):
    '''Create sticker'''
    model = Sticker

class StickerUpdateView(UpdateView):
    '''Update sticker when need'''
    model = Sticker
