from django.contrib import admin
from reports.models import Court, ServiceCentre, Repair, Device, Ticket

admin.site.register(Court)
admin.site.register(ServiceCentre)
admin.site.register(Repair)
admin.site.register(Device)
admin.site.register(Ticket)
