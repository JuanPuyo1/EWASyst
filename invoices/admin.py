from django.contrib import admin
from .models import InvoiceForItem, InvoiceForMaintenance, InvoiceForStone, Ring, ChainOrBracelet
# Register your models here.

admin.site.register(InvoiceForItem)
admin.site.register(InvoiceForMaintenance)
admin.site.register(InvoiceForStone)
admin.site.register(Ring)
admin.site.register(ChainOrBracelet)
