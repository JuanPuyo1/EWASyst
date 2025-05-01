
from django import forms
from .models import Invoice, InvoiceForItem, InvoiceForMaintenance, InvoiceForStone
from products.models import JewelleryItem, Stone


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        labels = {
            'client': 'Cliente',
            'invoice_number': 'Número de Factura',
            'invoice_type': 'Tipo de Factura',
            'invoice_date': 'Fecha de Factura',
            'invoice_status': 'Estado de Factura',
            'observation': 'Observación',
            'invoice_total': 'Total de Factura',
            'invoice_balance': 'Balance de Factura',
            'client_signature': 'Firma del Cliente',
        }
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'invoice_status', 'observation', 'invoice_total', 'invoice_balance', 'client_signature']

        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control'}),
            'invoice_status': forms.TextInput(attrs={'class': 'form-control'}),
            'observation': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_total': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_balance': forms.TextInput(attrs={'class': 'form-control'}),
            'client_signature': forms.FileInput(attrs={'class': 'form-control'}),
        }

class InvoiceForItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceForItem
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'invoice_status', 'observation', 'invoice_total', 'invoice_balance', 'client_signature', 'items']
        labels = {
            'client': 'Cliente',
            'invoice_number': 'Número de Factura',
            'invoice_type': 'Tipo de Factura',
            'invoice_date': 'Fecha de Factura',
            'invoice_status': 'Estado de Factura',
            'observation': 'Observación',
            'invoice_total': 'Total de Factura',
            'invoice_balance': 'Balance de Factura',
            'client_signature': 'Firma del Cliente',
            'items': 'Items',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control', 'value': 'Factura de Producto', 'readonly': True}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control'}),
            'invoice_status': forms.TextInput(attrs={'class': 'form-control'}),
            'observation': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_total': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_balance': forms.TextInput(attrs={'class': 'form-control'}),
            'client_signature': forms.FileInput(attrs={'class': 'form-control'}),
            'items': forms.SelectMultiple(attrs={
                'class': 'form-control select2',  # Add select2 class here
                'multiple': 'multiple'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['invoice_number'].initial = '25' + str(InvoiceForItem.objects.count() + 1)

class InvoiceForMaintenanceForm(InvoiceForm):
    class Meta:
        model = InvoiceForMaintenance
        fields = ['description']
        labels = {
            'description': 'Descripción',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InvoiceForStoneForm(InvoiceForm):
    class Meta:
        model = InvoiceForStone
        fields = ['stone']
        labels = {
            'stone': 'Piedra',
        }
        widgets = {
            'stone': forms.Select(attrs={'class': 'form-control'}),
        }





