from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name
