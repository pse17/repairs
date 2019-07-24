'''
Forms to display the models of application "reports"
'''

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput
from reports.models import Ticket, Device, Repair, ServiceCentre, Court

class TicketStateCOForm(ModelForm):
    ''' Form to edit CO-7/CO-8 state'''
    class Meta:
        model = Ticket
        fields = ['ticket', 'co7_state', 'co8_state', 'co41_state', 'co42_state', 'co7_date', 'co8_date']



class TicketOtherForm(ModelForm):
    '''Form to edit other fiels in Ticket model'''
    class Meta:
        model = Ticket
        fields = ['ticket', 'kind', 'location', 'remark', 'died']

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
        fields = ['sc_ticket', 'diagnostic_card', 'price', 'payment_method', 'warranty']

RepairFormSet = inlineformset_factory(Repair, Ticket, fields=('ticket',))

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
