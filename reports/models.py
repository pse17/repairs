''' Describe models application'''
from django.db import models

# Create your models here.

class Documents(models.Model):
    '''Model representing technical condition reports (in form CO-7, CO-8, CO-4.1, CO-4.2)'''

    NOT_DEFINED = 'n'
    IN_COURT = 'c'
    IN_DEP = 'd'
    IN_IAC = 'i'
    VERIFIED = 'v'
    REPORT_STATE = (
        (NOT_DEFINED, 'Не определен'),
        (IN_COURT, 'На подписании в суде'),
        (IN_DEP, 'На подписании в УСД'),
        (IN_IAC, 'На подписании ИАЦ'),
        (VERIFIED, 'Подписан'),
    )
    co7_state = models.CharField(
        max_length=1, choices=REPORT_STATE, blank=True, default=NOT_DEFINED)
    co8_state = models.CharField(
        max_length=1, choices=REPORT_STATE, blank=True, default=NOT_DEFINED)
    co41_state = models.CharField(
        max_length=1, choices=REPORT_STATE, blank=True, default=NOT_DEFINED)
    co42_state = models.CharField(
        max_length=1, choices=REPORT_STATE, blank=True, default=NOT_DEFINED)

    co7_date = models.DateField(null=True, blank=True)
    co8_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """ String for representing the Documents"""
        return 'CO-7 %s, CO-8 %s' % (self.co7_state, self.co8_state)

class Court(models.Model):
    '''Model representing court'''
    id = models.CharField(max_lenght=8, primary_key=True, db_index=True)
    name = models.CharField(max_lenght=80, null=True, blank=True)

    def __str__(self):
        """ String for representing the Court"""
        return self.name

class ServiceCentre(models.Model):
    '''Model representing service centre'''
    name = models.CharField(max_lenght=80, null=True, blank=True) 

    def __str__(self):
        """ String for representing the service centre"""
        return self.name

class Repair(models.Model):
    '''Model representing repair in service centre in case difficult repair'''

    tiket = models.CharField(max_lenght=8, help_text='Ticket in service centre')
    diagnostic_card = models.CharField(max_lenght=8, help_text='diagnostic card number')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    sc = models.ForeignKey(ServiceCentre, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """ String for representing repairs in service centre"""
        return '%s %s' % (self.diagnostic_card, self.price)

class Tickets(models.Model):
    '''Model representing ticket in IAC'''
    court = models.ForeignKey(Court, on_delete=models.SET_NULL, null=True, blank=True)

    NOT_DEFINED = 'n'
    SERVICE_CENTRE = 'c'
    REPAIR_KIT = 'k'
    NO_PAY = 'p'
    NO_REPAIR = 'r'
    KIND_OF_REPAIR = (
        (NOT_DEFINED, 'Не определено'),
        (SERVICE_CENTRE,'В сервисном центре'),
        (REPAIR_KIT,'С использованием ЗИП'),
        (NO_PAY, 'Мелкий ремонт без затрат'),
        (NO_REPAIR, 'Ремонт не выполнен'),
    )
    kind = models.CharField(
        max_length=1, choices=KIND_OF_REPAIR, blank=True, default=NOT_DEFINED)
