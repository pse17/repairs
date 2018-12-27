''' Describe views application reports'''
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from reports.models import Tickets
from reports.forms import TicketsForm, DeviceForm, CourtForm

def index(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})

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

    if request.method == 'POST':

        ticket_form = TicketsForm(request.POST, instance=ticket)
        device_form = DeviceForm(request.POST, instance=device)
        court_form = CourtForm(request.POST, instance=court)

        if ticket_form.is_valid() and device_form.is_valid():
            dev = device_form.save()
            tic = ticket_form.save(commit=False)
            tic.device = dev
            tic.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        ticket_form = TicketsForm(instance=ticket)
        device_form = DeviceForm(instance=device)
        court_form = CourtForm(instance=court)

    return render(request, 'reports/ticket_edit.html', context={
        'ticket_form': ticket_form, 'device_form': device_form, 'court_form': court_form})
