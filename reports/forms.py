'''
Forms to display the models of application "reports"
'''

from django.forms import ModelForm
from django.forms.widgets import TextInput
from reports.models import Tickets, Device, Repair, ServiceCentre, Court

class TicketsStateCOForm(ModelForm):
    ''' Form to edit CO-7/CO-8 state'''
    class Meta:
        model = Tickets
        fields = ['ticket', 'co7_state', 'co8_state', 'co41_state', 'co42_state', 'co7_date', 'co8_date']
        widgets = {'ticket': TextInput(attrs={'disabled': True})}

class TicketsOtherForm(ModelForm):
    '''Form to edit other fiels in Tickets model'''
    class Meta:
        model = Tickets
        fields = ['ticket', 'kind', 'location', 'remark', 'died']
        widgets = {'ticket': TextInput(attrs={'disabled': True})}

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
