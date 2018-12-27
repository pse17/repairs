''' Describe URLs for application reports'''
from django.urls import path
from reports.views import index, TicketsListView, TicketsDetailView, ticket_edit


urlpatterns = [
    path('', index, name='index'),
    path('list/', TicketsListView.as_view(), name='tickets_list'),
    path('ticket/<int:pk>', TicketsDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/edit', ticket_edit, name='ticket_edit'),
]
