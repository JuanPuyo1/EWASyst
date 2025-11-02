from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.validators import RegexValidator
from django.db.models import Max
# Create your models here.

class Client(models.Model):
    def generate_document_number():
        # Get the last document number
        last_document = Client.objects.all().aggregate(Max('id'))['id__max']
        # If no documents exist, start with 1, else increment by 1
        next_number = 1 if last_document is None else last_document + 1
        # Format: EWA001, EWA002, etc.
        return f'EWA_default{next_number:03d}'
    


    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False, validators=[MinLengthValidator(3)])
    email = models.EmailField(null=True, blank=True, validators=[EmailValidator])
    phone = models.CharField(max_length=15, null=True, blank=True, validators=[MinLengthValidator(10), RegexValidator(r'^\d{10}$')])
    address = models.TextField(max_length=255, null=True, blank=True)

    DOCUMENT_TYPE_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('NIT', 'Número de Identificación Tributaria'),
        ('PAS', 'Pasaporte'),
    ]
    
    document_type = models.CharField(max_length=100, null=True, blank=True, choices=DOCUMENT_TYPE_CHOICES)
    document_number = models.CharField(max_length=100, unique=True, default=generate_document_number, validators=[RegexValidator(r'^\d{10}$')])
        
    def __str__(self):
        return self.name
