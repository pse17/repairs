from reports.models import Ticket
from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['ticket', 'court', 'name', 'invent_number', 'serial_number']
        depth = 1
    
