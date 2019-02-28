''' Describe URLs for application reports'''
from django.urls import path
from reports.views import home_view, TicketsListView, TicketsDetailView
from reports.views import TicketsStateCOView, TicketsOtherView, RepairUpdateView, RepairCreateView


urlpatterns = [
    path('', home_view, name='index'),
    path('list/', TicketsListView.as_view(), name='tickets_list'),
    path('ticket/<int:pk>', TicketsDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/co', TicketsStateCOView.as_view(), name='ticket_edit_co'),
    path('ticket/<int:pk>/other', TicketsOtherView.as_view(), name='ticket_edit_other'),
    path('repair/create/<int:pk>', RepairCreateView.as_view(), name='repair_create'),
    path('repair/<int:pk>', RepairUpdateView.as_view(), name='repair_update'),
]
