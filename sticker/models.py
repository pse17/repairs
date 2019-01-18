''' Model for sticker app. I`m captain obvious'''
from django.db import models
from reports.models import Court

class Sticker(models.Model):
    '''Model representing inscription on the sticker'''

    court = models.ForeignKey('reports.Court', related_name='courts', \
        on_delete=models.SET_NULL, null=True)
    device_name = models.CharField(max_length=80, null=False)
    invent_number = models.CharField(max_length=18, null=False)
    serial_number = models.CharField(max_length=24, blank=True)
    production_date = models.CharField(max_length=4, blank=True) # Year only
    malfunction = models.TextField(blank=True)
    delivery_date = models.DateField(auto_now=True) # When delivered to repair

    def __str__(self):
        """ String for representing Stiker """
        return '%s %s %s' % (self.device_name, self.invent_number, self.serial_number)
