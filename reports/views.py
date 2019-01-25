''' Describe views application reports'''
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from reports.forms import  TicketsStateCOForm, TicketsOtherForm
from reports.models import Tickets

def home_view(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})

class TicketsListView(ListView):
    ''' Displays ttickets list '''
    model = Tickets

class TicketsDetailView(PermissionRequiredMixin, DetailView):
    ''' Displays detailed ticket info'''
    model = Tickets
    permission_required = 'tickeets.can_edit_ticket'

class TicketsStateCOView(PermissionRequiredMixin, FormView):
    ''' Edit some fields ) '''
    template_name = 'tickets_CO.html'
    form_class = TicketsStateCOForm
    success_url = reverse_lazy('tickets_list')
    permission_required = 'tickeets.can_edit_ticket'

class TicketsOtherView(PermissionRequiredMixin, FormView):
    ''' Edit some other fields ) '''
    template_name = 'tickets_other.html'
    form_class = TicketsOtherForm
    success_url = reverse_lazy('tickets_list')
    permission_required = 'tickeets.can_edit_ticket'
