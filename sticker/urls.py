''' Describe URLs for application sticker'''
from django.urls import path
from sticker.views import StickerListView, StickerCreateView, StickerUpdateView, StickerDetailView

urlpatterns = [
    path('list/', StickerListView.as_view(), name='sticker_list'),
    path('create/', StickerCreateView.as_view(), name='sticker_create'),
    path('update/<int:pk>', StickerUpdateView.as_view(), name='sticker_update'),
    path('detail/<int:pk>', StickerDetailView.as_view(), name='sticker_detail'),
]
