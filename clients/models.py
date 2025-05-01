from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, validators=[MinLengthValidator(3)])
    email = models.EmailField(null=False, blank=False, validators=[EmailValidator])
    phone = models.CharField(max_length=15, null=False, blank=False, validators=[MinLengthValidator(10), RegexValidator(r'^\d{10}$')])
    address = models.TextField(max_length=255, null=True, blank=True)

    DOCUMENT_TYPE_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('NIT', 'Número de Identificación Tributaria'),
        ('PAS', 'Pasaporte'),
    ]
    
    document_type = models.CharField(max_length=100, null=True, blank=True, choices=DOCUMENT_TYPE_CHOICES)
    document_number = models.CharField(max_length=100, null=True, blank=True, validators=[RegexValidator(r'^\d{10}$')])
        
    def __str__(self):
        return self.name
