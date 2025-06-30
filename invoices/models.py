from django.db import models
from django.utils import timezone
from clients.models import Client

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
    
    invoice_quantity = models.IntegerField(null=True, blank=True)
    
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    invoice_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Factura {self.pk}"

    def check_invoice_status(self):
        if self.invoice_balance > 0:
            self.invoice_status = 'Pendiente de Pago'
        else:
            self.invoice_status = 'Pagado'
        self.save()


