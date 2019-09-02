''' Describe views application reports'''
from time import strftime
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from reports.forms import  RepairForm, RepairFormSet
from reports.models import Ticket, Repair
import reports.replicate as replicate


def home_view(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})


class TicketListView(ListView):
    ''' Displays tTicket list '''
    model = Ticket

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(year=2019).extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('-int')

class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ['co7_state', 'co8_state', 'kind', 'location', 'died']
    success_url = reverse_lazy('tickets_list')

    def get_context_data(self, **kwargs):
        context = super(TicketUpdateView, self).get_context_data(**kwargs)
        context['ticket_id'] = self.object.ticket
        context['court_name'] = self.object.court.name
        context['co7_date'] = self.object.co7_date.strftime('%d/%m/%Y')
        context['name'] = self.object.name
        context['invent_number'] = self.object.invent_number
        context['serial_number'] = self.object.serial_number
        context['remark'] = self.object.remark
        
        
        if self.object.co8_date is not None:
            context['co8_date'] = self.object.co8_date.strftime('%d/%m/%Y')
        else:
            context['co8_date'] = ' '*10
        return context


class RepairUpdateView(UpdateView):
    ''' Edit repair details '''
    model = Repair
    form_class = RepairForm
    template_name = 'reports/repair_update.html'
    success_url = reverse_lazy('Ticket_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = Ticket.objects.get(repair=self.kwargs['pk'])
        return context


class RepairCreateView(CreateView):
    ''' Create repair details '''
    model = Repair
    form_class = RepairForm
    template_name = 'reports/repair_update.html'
    success_url = reverse_lazy('Ticket_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = Ticket.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        self.object = form.save()
        ticket = Ticket.objects.get(pk=self.kwargs['pk'])
        ticket.repair = self.object
        ticket.save()
        return super().form_valid(form)


class CO7IsMissReport(ListView):
    ''' Report "CO7 is missing" '''
    model = Ticket
    template_name = 'reports/ticket_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(co7_state='v')
        queryset = queryset.extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('int')
        return queryset

class CO8IsMissReport(ListView):
    ''' Report "CO8 is missing" '''
    model = Ticket
    template_name = 'reports/ticket_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(co8_state='v')
        queryset = queryset.extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('int')
        return queryset

class TypeIsMissReport(ListView):
    ''' Report "repair type is missing" '''
    model = Ticket
    template_name = 'reports/ticket_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(kind='n')
        queryset = queryset.extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('int')
        return queryset


class RepairKitReport(ListView):
    ''' Repair kit report by the current month '''
    model = Ticket
    template_name = 'reports/ticket_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(kind='k')
        queryset = queryset.filter(co8_date__month=datetime.now().month)
        queryset = queryset.extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('int')
        return queryset


def replicate_view(request):
    ''' Run replicate only'''
    replicate.main()
    return render(request, 'reports/index.html', context={})
