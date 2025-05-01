from django.db import models
from django.utils import timezone
from clients.models import Client
from products.models import JewelleryItem, Stone

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    invoice_type = models.CharField(max_length=100, null=True, blank=True)
    invoice_date = models.DateField(null=False, blank=False, default=timezone.now)

    INVOICE_STATUS_CHOICES = [
        ('Pendiente de Pago', 'Pendiente de Pago'),
        ('Pagado', 'Pagado'),
        ('Cancelado', 'Cancelado'),
    ]

    invoice_status = models.CharField(max_length=100, null=True, blank=True, choices=INVOICE_STATUS_CHOICES, default='Pendiente de Pago')
    observation = models.TextField(null=True, blank=True)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    invoice_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True 

    def __str__(self):
        return self.pk

    def check_invoice_status(self):
        if self.invoice_balance > 0:
            self.invoice_status = 'Pendiente de Pago'
        else:
            self.invoice_status = 'Pagado'
        self.save()

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


class InvoiceForCustomized(Invoice):
    description = models.TextField()
    def __str__(self):
        return f"Factura de Joyas a medida {self.pk}"


