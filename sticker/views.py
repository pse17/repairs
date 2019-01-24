from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from sticker.models import Sticker
from sticker.forms import StickerForm

class StickerListView(ListView):
    ''' Displays stickers list '''
    model = Sticker

class StickerCreateView(PermissionRequiredMixin, CreateView):
    '''Create sticker'''
    form_class = StickerForm
    success_url = '/sticker/list/'
    template_name = 'sticker/sticker_create.html'
    permission_required = 'sticker.can_make_sticker'

class StickerUpdateView(PermissionRequiredMixin, UpdateView):
    '''Update sticker when need'''
    form_class = StickerForm
    model = Sticker
    template_name = 'sticker/sticker_update.html'
    success_url = reverse_lazy('sticker_list')
    permission_required = 'sticker.can_make_sticker'

class StickerDetailView(PermissionRequiredMixin, DetailView):
    '''Detail stiker view for print'''
    model = Sticker
    permission_required = 'sticker.can_make_sticker'
