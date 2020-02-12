''' Describe URLs for application sticker'''
from django.urls import path
from sticker.api import *
from sticker.views import *

urlpatterns = [
    path('list/', StickerListView.as_view(), name='sticker_list'),
    path('create/', StickerCreateView.as_view(), name='sticker_create'),
    path('update/<int:pk>', StickerUpdateView.as_view(), name='sticker_update'),
    path('detail/<int:pk>', StickerDetailView.as_view(), name='sticker_detail'),
]

urlpatterns += [
    path('api/list', StickerList.as_view(), name='list_sticker'),
    path('api/add', StickerAdd.as_view(), name='add_sticker'),
    path('api/<int:pk>', StickerUpdate.as_view(), name='update_sticker'),
    path('api/court', CourtList.as_view(), name='list_court')
]