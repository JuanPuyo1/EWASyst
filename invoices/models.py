from django.db import models
from clients.models import Client

class JewelleryItem(models.Model):
    jewellery_name = models.CharField(max_length=100)
    jewellery_quantity = models.IntegerField()
    certificate = models.BooleanField(default=False)


    def __str__(self):
        return self.jewellery_name


class Stone(models.Model):
    stone_name = models.CharField(max_length=100)
    stone_color = models.CharField(max_length=100)
    stone_clarity = models.CharField(max_length=100)
    stone_carat = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.stone_name

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


class Ring(JewelleryItem):
    ring_size = models.CharField(max_length=100)
    ring_type = models.CharField(max_length=100)
    ring_quality = models.CharField(max_length=100)
    ring_weight = models.DecimalField(max_digits=10, decimal_places=2)
    stone = models.ForeignKey(Stone, on_delete=models.DO_NOTHING, null=True, blank=True)
    synthetic_stone = models.BooleanField(default=False)
    def __str__(self):
        return self.ring_type


class ChainOrBracelet(JewelleryItem):
    chain_or_bracelet_weight = models.DecimalField(max_digits=10, decimal_places=2)
    chain_or_bracelet_quality = models.CharField(max_length=100)
    long = models.DecimalField(max_digits=10, decimal_places=2)
    fabric = models.CharField(max_length=100)
    def __str__(self):
        return self.chain_or_bracelet_quality


