
from django import forms
from .models import InvoiceForItem, InvoiceForMaintenance, Diamond, Ring, Emerald

class InvoiceForItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceForItem
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'invoice_status', 'items']

class InvoiceForMaintenanceForm(forms.ModelForm):
    class Meta:
        model = InvoiceForMaintenance
        fields = ['client', 'invoice_number', 'invoice_date', 'invoice_status', 'description']


class DiamondForm(forms.ModelForm):
    class Meta:
        model = Diamond
        fields = ['diamond_name', 'diamond_shape', 'diamond_color', 'diamond_clarity', 'diamond_carat', 'diamond_price', 'diamond_total']

class RingForm(forms.ModelForm):
    class Meta:
        model = Ring
        fields = ['ring_name', 'ring_size', 'ring_price', 'ring_total', 'ring_type']

class EmeraldForm(forms.ModelForm):
    class Meta:
        model = Emerald
        fields = ['emerald_name', 'emerald_color', 'emerald_clarity', 'emerald_carat', 'emerald_price', 'emerald_total']

