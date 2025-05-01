from django.db import models
from clients.models import Client
from products.models import JewelleryItem, Stone

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    invoice_type = models.CharField(max_length=100, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    invoice_status = models.CharField(max_length=100, null=True, blank=True)
    observation = models.TextField(null=True, blank=True)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    invoice_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    client_signature = models.ImageField(upload_to='uploads/client_signatures/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True 

    def __str__(self):
        return self.pk

class InvoiceForItem(Invoice):
    
    items = models.ManyToManyField(JewelleryItem, related_name='items', blank=True)        


    def __str__(self):
        return f"Factura de Item {self.pk}"

class InvoiceForMaintenance(Invoice):
    description = models.TextField()
    def __str__(self):
        return f"Factura de Mantenimiento {self.pk}"


class InvoiceForStone(Invoice):
    stone = models.ForeignKey(Stone, on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return f"Factura de Piedra {self.pk}"




