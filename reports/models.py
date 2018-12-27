''' Describe application models'''
from django.db import models
from django.urls import reverse

class Court(models.Model):
    '''Model representing court'''
    id = models.CharField(max_length=8, primary_key=True, db_index=True)
    name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        """ String for representing the Court"""
        return self.name

class ServiceCentre(models.Model):
    '''Model representing service centre'''
    name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        """ String for representing the service centre"""
        return self.name

class Repair(models.Model):
    '''Model representing repair in service centre in case difficult repair'''

    sc = models.ForeignKey(ServiceCentre, on_delete=models.SET_NULL, null=True, blank=True)
    ticket = models.CharField(max_length=8, null=True, help_text='Ticket in service centre')
    diagnostic_card = models.CharField(max_length=8, null=True, help_text='diagnostic card number')
    price = models.DecimalField(max_digits=9, null=True, decimal_places=2)
    warranty = models.BooleanField(null=True, default=False)

    CASH = 'h'
    CASHLESS = 's'
    PAYMENT_METHOD = (
        (CASH, 'Наличный'),
        (CASHLESS, 'Безналичный')
    )
    payment_method = models.CharField(
        max_length=1, choices=PAYMENT_METHOD, blank=True, default=CASHLESS)


    def __str__(self):
        """ String for representing repairs in service centre"""
        return '%s %s' % (self.diagnostic_card, self.price)

class Device(models.Model):
    '''Model representing device which we repair'''
    name = models.CharField(max_length=80, null=True, blank=True)
    invent_number = models.CharField(
        max_length=18, null=True, blank=True, db_index=True)
    serial_number = models.CharField(
        max_length=24, null=True, blank=True, db_index=True)

    def __str__(self):
        """ String for representing device"""
        return '%s %s %s' % (self.name, self.invent_number, self.serial_number)

class Tickets(models.Model):
    '''Model representing ticket in IAC'''
    ticket = models.CharField(max_length=6, db_index=True)
    court = models.ForeignKey(Court, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, blank=True)
    repair = models.ForeignKey(Repair, on_delete=models.SET_NULL, null=True, blank=True)

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

    SERVICE_CENTRE = 'c'
    REPAIR_KIT = 'k'
    NO_PAY = 'p'
    NO_REPAIR = 'r'
    KIND_OF_REPAIR = (
        (NOT_DEFINED, 'Не определено'),
        (SERVICE_CENTRE, 'В сервисном центре'),
        (REPAIR_KIT, 'С использованием ЗИП'),
        (NO_PAY, 'Мелкий ремонт без затрат'),
        (NO_REPAIR, 'Ремонт не выполнен'),
    )
    kind = models.CharField(
        max_length=1, choices=KIND_OF_REPAIR, blank=True, default=NOT_DEFINED)

    COURT = 'c' # In court. Not yet repair or already fixed.
    IAC = 'i'   # In IAC. For diagnostic or already fixed.
    SC = 's'    # In service centre.
    DEVICE_LOCATION = (
        (COURT, 'В суде'),
        (IAC, 'В ИАЦ'),
        (SC, 'В сервисном центре'),
    )
    location = models.CharField(
        max_length=1, choices=DEVICE_LOCATION, blank=True, default=COURT)
    remark = models.CharField(max_length=100, null=True, help_text='Device malfunction describe')
    died = models.BooleanField(default=False, help_text='Repair impossible')

    class Meta:
        ordering = ["ticket"]

    def __str__(self):
        """ String for representing ticket"""
        return self.ticket

    def get_absolute_url(self):
        ''' Returns the url to access a particular ticket instance '''
        return reverse('ticket_detail', args=[str(self.id)])
