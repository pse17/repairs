'''
Forms to display the models of application "reports"
'''

from django.forms import ModelForm
from django.forms.widgets import DateInput, SelectDateWidget, TextInput
from django.contrib.admin.widgets import AdminDateWidget
from reports.models import Tickets, Device, Repair, ServiceCentre, Court

class TicketsForm(ModelForm):
    ''' Form to display the model Tickets '''
    class Meta:
        model = Tickets
        fields = [
            'ticket', 'co7_state', 'co8_state', 'co41_state', 'co42_state',
            'co7_date', 'co8_date', 'kind', 'location', 'remark', 'died',
        ]
        widgets = {
            'co7_date': DateInput,
            'ticket': TextInput(attrs={'size': 6, 'disabled': True}),
        }

class DeviceForm(ModelForm):
    ''' Form to display the model Device '''
    class Meta:
        model = Device
        fields = ['name', 'invent_number', 'serial_number']
        widgets = {
            'name': TextInput(attrs={'size': 80, 'disabled': True}),
            'invent_number': TextInput(attrs={'size': 14, 'disabled': True}),
            'serial_number': TextInput(attrs={'size': 20, 'disabled': True}),
        }

class RepairForm(ModelForm):
    ''' Form to display the model Repair '''
    class Meta:
        model = Repair
        fields = ['sc_ticket', 'diagnostic_card', 'price', 'warranty']

class ServiceCentreForm(ModelForm):
    ''' Form to display the model ServiceCentre '''
    class Meta:
        model = ServiceCentre
        fields = ['name']

class CourtForm(ModelForm):
    ''' Form to display the model Court '''
    class Meta:
        model = Court
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'size': 80, 'disabled': True}),
        }
