''' Model for sticker app. I`m captain obvious'''
from django.db import models


class CourtForSticker(models.Model):
    '''Model representing court'''
    id = models.CharField(max_length=8, primary_key=True, db_index=True)
    name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        """ String for representing the Court"""
        return self.name


class Sticker(models.Model):
    '''Model representing inscription on the sticker'''
    court = models.ForeignKey(CourtForSticker,on_delete=models.SET_NULL, null=True)
    device_name = models.CharField(max_length=80, null=True, blank=True)
    invent_number = models.CharField(max_length=18, null=True, blank=True)
    serial_number = models.CharField(max_length=24, null=True, blank=True)
    production_date = models.CharField(max_length=4, null=True, blank=True) # Year only
    malfunction = models.TextField(null=True, blank=True)
    delivery_date = models.DateField(auto_now=True) # When delivered to repair

    class Meta:
        ordering = ["-delivery_date"]

    def __str__(self):
        """ String for representing Stiker """
        return '%s %s %s' % (self.device_name, self.invent_number, self.serial_number)
