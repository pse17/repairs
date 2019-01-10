'''
Forms to display the models of application "reports"
'''

from django.forms import ModelForm
from django.forms.widgets import DateInput, SelectDateWidget
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
        }

class DeviceForm(ModelForm):
    ''' Form to display the model Device '''
    class Meta:
        model = Device
        fields = ['name', 'invent_number', 'serial_number']

class RepairForm(ModelForm):
    ''' Form to display the model Repair '''
    class Meta:
        model = Repair
        fields = ['ticket', 'diagnostic_card', 'price', 'warranty']

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
