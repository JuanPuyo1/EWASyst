from django.db import models

# Create your models here.
class JewelleryItem(models.Model):
    jewellery_description = models.CharField(max_length=100, null=True, blank=True)
    jewellery_quantity = models.IntegerField(null=True, blank=True)
    certificate = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.jewellery_description


class Stone(models.Model):
    stone_color = models.CharField(max_length=100, null=True, blank=True)
    stone_clarity = models.CharField(max_length=100, null=True, blank=True)
    stone_carat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Piedra'
        verbose_name_plural = 'Piedras'

    def __str__(self):
        return self.stone_color or self.jewellery_description
    

class Ring(JewelleryItem):
    ring_size = models.CharField(max_length=100, null=True, blank=True)

    RING_TYPE_CHOICES = [
        ('Anillo de Compromiso', 'Anillo de Compromiso'),
        ('Anillo de Matrimonio mujer', 'Anillo de Matrimonio mujer'),
        ('Anillo de Matrimonio hombre', 'Anillo de Matrimonio hombre'),
        ('Anillo de Regalo mujer', 'Anillo de Regalo mujer'),
        ('Anillo de Regalo hombre', 'Anillo de Regalo hombre'),
    ]
    ring_type = models.CharField(max_length=100, null=True, blank=True, choices=RING_TYPE_CHOICES)
    RING_QUALITY_CHOICES = [
        ('Oro amarillo 18k', 'Oro amarillo 18k'),
        ('Oro blanco 18k', 'Oro blanco 18k'),
        ('Oro rosa 18k', 'Oro rosa 18k'),
        ('Plata 950', 'Plata 950'),        
    ]
    ring_quality = models.CharField(max_length=100, null=True, blank=True, choices=RING_QUALITY_CHOICES)
    synthetic_stone = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/images/rings/', null=True, blank=True)
    def __str__(self):
        return self.ring_type


class ChainOrBracelet(JewelleryItem):
    chain_or_bracelet_quality = models.CharField(max_length=100, null=True, blank=True)
    long = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fabric = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.chain_or_bracelet_quality