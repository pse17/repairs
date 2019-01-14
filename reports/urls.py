''' Describe URLs for application reports'''
from django.urls import path
from reports.views import index, TicketsListView,\
    TicketsDetailView, TicketsStateCOView, TicketsOtherView


urlpatterns = [
    path('', index, name='index'),
    path('list/', TicketsListView.as_view(), name='tickets_list'),
    path('ticket/<int:pk>', TicketsDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/co', TicketsStateCOView.as_view(), name='ticket_edit_co'),
    path('ticket/<int:pk>/other', TicketsOtherView.as_view(), name='ticket_edit_other'),
]
