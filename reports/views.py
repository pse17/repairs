''' Describe views application reports'''
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from reports.models import Tickets, Repair
from reports.forms import DeviceForm, CourtForm, RepairForm, TicketsStateCOForm, TicketsOtherForm

def home_view(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})

class TicketsListView(ListView):
    ''' Displays ttickets list '''
    model = Tickets

class TicketsDetailView(DetailView):
    ''' Displays detailed ticket info'''
    model = Tickets

class TicketsStateCOView(FormView):
    ''' Edit some fields ) '''
    template_name = 'tickets_CO.html'
    form_class = TicketsStateCOForm
    success_url = reverse_lazy('tickets_list')

class TicketsOtherView(FormView):
    ''' Edit some other fields ) '''
    template_name = 'tickets_other.html'
    form_class = TicketsOtherForm
    success_url = reverse_lazy('tickets_list')

'''
def ticket_edit_form(request, pk):
    Edit a particular ticket instance

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
'''