''' Describe views application reports'''
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from reports.models import Tickets, Repair
from reports.forms import TicketsForm, DeviceForm, CourtForm, RepairForm

def index(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})

def ticket_detail_view(request, pk):
    ticket = Tickets.objects.get(pk=pk)

class TicketsListView(ListView):
    ''' Displays ttickets list '''
    model = Tickets

class TicketsDetailView(DetailView):
    ''' Displays detailed ticket info'''
    model = Tickets

def ticket_edit_form(request, pk):
    ''' Edit a particular ticket instance '''

    ticket = Tickets.objects.get(pk=pk)
    device = ticket.device
    court = ticket.court

    if ticket.repair:
        # If there is data on repair in the service center
        repair = ticket.repair
    else:
        repair = Repair(sc_ticket='0', diagnostic_card='0', price=0, warranty=False)

    if request.method == 'POST':

        ticket_form = TicketsForm(request.POST, instance=ticket)
        device_form = DeviceForm(request.POST, instance=device)
        court_form = CourtForm(request.POST, instance=court)
        repair_form = RepairForm(request.POST, instance=repair)

        if ticket_form.is_valid():
            ticket_form.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        ticket_form = TicketsForm(instance=ticket)
        device_form = DeviceForm(instance=device)
        court_form = CourtForm(instance=court)
        repair_form = RepairForm(instance=repair)

    return render(request, 'reports/ticket_edit.html', context={
        'ticket_form': ticket_form,
        'device_form': device_form,
        'court_form': court_form,
        'repair_form': repair_form})
