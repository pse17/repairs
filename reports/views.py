''' Describe views application reports'''
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.forms import inlineformset_factory
from reports.models import Tickets, Device, Court

def index(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})

class TicketsListView(ListView):
    ''' Displays ttickets list '''
    model = Tickets

class TicketsDetailView(DetailView):
    ''' Displays detailed ticket info'''
    model = Tickets

def ticket_edit(request, pk):
    ''' Edit a particular ticket instance '''
    tickets_inline_form_set = inlineformset_factory(Device, Tickets, fields=('device_set.name', 'ticket'))
    ticket = Tickets.objects.get(pk=pk)
    if request.method == 'POST':
        formset = tickets_inline_form_set(request.POST, instance=ticket)
        if formset.is_valid():
            formset.save()
            return reverse('index')
    else:
        formset = tickets_inline_form_set(instance=ticket)
    return render('ticket_edit.html', {'formset': formset,})
