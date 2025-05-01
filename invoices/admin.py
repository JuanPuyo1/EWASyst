from django.contrib import admin
from .models import InvoiceForItem, InvoiceForMaintenance, InvoiceForStone, InvoiceForCustomized
# Register your models here.

admin.site.register(InvoiceForItem)
admin.site.register(InvoiceForMaintenance)
admin.site.register(InvoiceForStone)
admin.site.register(InvoiceForCustomized)
