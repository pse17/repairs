''' Describe views application reports'''
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from reports.forms import  TicketsStateCOForm, TicketsOtherForm, RepairForm, RepairFormSet
from reports.models import Tickets, Repair
import reports.replicate as repl

def home_view(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})


class TicketsListView(ListView):
    ''' Displays ttickets list '''
    model = Tickets

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(year=2019).extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('-int')


class TicketsDetailView(PermissionRequiredMixin, DetailView):
    ''' Displays detailed ticket info'''
    model = Tickets
    permission_required = 'tickeets.can_edit_ticket'


class TicketsStateCOView(UpdateView):
    ''' Edit some fields ) '''
    model = Tickets
    template_name = 'reports/tickets_CO.html'
    form_class = TicketsStateCOForm
    success_url = reverse_lazy('tickets_list')


class TicketsOtherView(UpdateView):
    ''' Edit some other fields ) '''
    model = Tickets
    template_name = 'reports/tickets_other.html'
    form_class = TicketsOtherForm
    success_url = reverse_lazy('tickets_list')


class RepairUpdateView(UpdateView):
    ''' Edit repair details '''
    model = Repair
    form_class = RepairForm
    template_name = 'reports/repair_update.html'
    success_url = reverse_lazy('tickets_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = Tickets.objects.get(repair=self.kwargs['pk'])
        return context


class RepairCreateView(CreateView):
    ''' Create repair details '''
    model = Repair
    form_class = RepairForm
    template_name = 'reports/repair_update.html'
    success_url = reverse_lazy('tickets_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = Tickets.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        self.object = form.save()
        ticket = Tickets.objects.get(pk=self.kwargs['pk'])
        ticket.repair = self.object
        ticket.save()
        return super().form_valid(form)


class CO7IsMissReport(ListView):
    ''' Report "CO7 is missing" '''
    model = Tickets
    template_name = 'reports/miss-co7.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(co7_state='v')
        queryset = queryset.extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('int')
        return queryset


class TypeIsMissReport(ListView):
    ''' Report "repair type is missing" '''
    model = Tickets
    template_name = 'reports/tickets_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(kind='n')
        queryset = queryset.extra(select={'int': 'CAST(ticket AS INTEGER)'}).order_by('int')
        return queryset


def replicate_view(request):
    ''' Run replicate only'''
    repl.main()
    return render(request, 'reports/index.html', context={})
