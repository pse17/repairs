''' Describe URLs for application reports'''
from django.urls import path
from reports.views import *



urlpatterns = [
    path('', home_view, name='index'),
    path('list/', TicketListView.as_view(), name='tickets_list'),
    path('ticket/update/<int:pk>', TicketUpdateView.as_view(), name='ticket-update'),
    path('repair/create/<int:pk>', RepairCreateView.as_view(), name='repair_create'),
    path('repair/<int:pk>', RepairUpdateView.as_view(), name='repair_update'),
    path('co7miss', CO7IsMissReport.as_view(), name='co7miss'),
    path('co8miss', CO8IsMissReport.as_view(), name='co8miss'),
    path('typemiss', TypeIsMissReport.as_view(), name='typemiss'),
    path('replicate', replicate_view, name='replicate'),
]
