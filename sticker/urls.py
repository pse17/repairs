''' Describe URLs for application sticker'''
from django.urls import path
from sticker.views import StickerListView, StickerCreateView, StickerUpdateView

urlpatterns = [
    path('list/', StickerListView.as_view(), name='sticker_list'),
    path('sticker/<int:pk>/create/', StickerCreateView.as_view(), name='sticker_create'),
    path('sticker/<int:pk>/update/', StickerUpdateView.as_view(), name='sticker_update')
]
