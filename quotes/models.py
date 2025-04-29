from django.db import models
from clients.models import Client
from django.utils.crypto import get_random_string
# Create your models here.

class Quote(models.Model):
    quote_number = models.CharField(max_length=100, null=True, blank=True, unique=True, default='EWA'+get_random_string(length=3))
    quote_quantity = models.IntegerField(null=True, blank=True)
    quote_date = models.DateField(null=True, blank=True)
    quote_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quote_description = models.TextField(null=True, blank=True)
    quote_details = models.CharField(max_length=100, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)
    def __str__(self):
        return self.quote_number

