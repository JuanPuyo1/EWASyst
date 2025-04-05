from django.contrib import admin
from .models import InvoiceForItem, InvoiceForMaintenance, InvoiceForStone, Ring, ChainOrBracelet, Stone, JewelleryItem 
# Register your models here.

admin.site.register(InvoiceForItem)
admin.site.register(InvoiceForMaintenance)
admin.site.register(InvoiceForStone)
admin.site.register(JewelleryItem)
admin.site.register(Ring)
admin.site.register(Stone)
admin.site.register(ChainOrBracelet)
