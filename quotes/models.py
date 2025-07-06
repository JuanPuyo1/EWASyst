from django.db import models
from clients.models import Client
from django.utils import timezone
from django.db.models import Max

# Create your models here.



class Quote(models.Model):
    def generate_quote_number():
        # Get the last quote number
        last_quote = Quote.objects.all().aggregate(Max('id'))['id__max']
        # If no quotes exist, start with 1, else increment by 1
        next_number = 1 if last_quote is None else last_quote + 1
        # Format: EWA001, EWA002, etc.
        return f'EWA{next_number:03d}'

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    quote_number = models.CharField(
        max_length=100, 
        unique=True, 
        default=generate_quote_number,
    )
    
    quote_quantity = models.IntegerField(null=True, blank=True)

    QUOTE_PRODUCT_TYPE_CHOICES = [
        ('Anillo de Compromiso', 'Anillo de Compromiso'),
        ('Anillo de Matrimonio', 'Anillo de Matrimonio'),
        ('A medida', 'A medida'),
        ('Otro', 'Otro'),
    ]

    quote_product_type = models.CharField(max_length=100, null=False, blank=False, choices=QUOTE_PRODUCT_TYPE_CHOICES)
    quote_date = models.DateField(null=False, blank=False, default=timezone.now)
    quote_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quote_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quote_description = models.TextField(null=True, blank=True)
    quote_additional_notes = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)


    quote_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quote_discount_description = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.quote_number

