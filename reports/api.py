from django.http import Http404
from reports.models import Ticket
from reports.serializers import TicketSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class TicketAPI(APIView):
    ''' Retrieve, update ticket '''

    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Exception:
            raise Http404
    
    def get(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketListAPI(APIView):
    ''' List tickets '''
    def get(self, request, format=None):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)
