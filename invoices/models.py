from django.db import models
from clients.models import Client

class JewelleryItem(models.Model):
    jewellery_name = models.CharField(max_length=100)
    jewellery_quantity = models.IntegerField()
    jewellery_price = models.DecimalField(max_digits=10, decimal_places=2)
    jewellery_total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.jewellery_name

class InvoiceForItem(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100)
    invoice_type = models.CharField(max_length=100)
    invoice_date = models.DateField()
    invoice_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(JewelleryItem)    
    def __str__(self):
        return self.invoice_number

class InvoiceForMaintenance(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    invoice_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    def __str__(self):
        return self.invoice_number

class Diamond(JewelleryItem):
    diamond_name = models.CharField(max_length=100)
    diamond_shape = models.CharField(max_length=100)
    diamond_color = models.CharField(max_length=100)
    diamond_clarity = models.CharField(max_length=100)
    diamond_carat = models.DecimalField(max_digits=10, decimal_places=2)
    diamond_price = models.DecimalField(max_digits=10, decimal_places=2)
    diamond_total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.diamond_name

class Ring(JewelleryItem):
    ring_name = models.CharField(max_length=100)
    ring_size = models.CharField(max_length=100)
    ring_price = models.DecimalField(max_digits=10, decimal_places=2)
    ring_total = models.DecimalField(max_digits=10, decimal_places=2)
    ring_type = models.CharField(max_length=100)
    def __str__(self):
        return self.ring_name

class Emerald(JewelleryItem):
    emerald_name = models.CharField(max_length=100)
    emerald_color = models.CharField(max_length=100)
    emerald_clarity = models.CharField(max_length=100)
    emerald_carat = models.DecimalField(max_digits=10, decimal_places=2)
    emerald_price = models.DecimalField(max_digits=10, decimal_places=2)
    emerald_total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.emerald_name
