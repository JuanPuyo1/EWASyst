
from django import forms
from .models import Invoice, InvoiceForItem, InvoiceForMaintenance, InvoiceForStone, InvoiceForCustomized
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
            'additional_notes': 'Notas Adicionales',
            'invoice_total': 'Total de Factura',
            'invoice_balance': 'Balance de Factura',
        }
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'invoice_status', 'observation', 'additional_notes', 'invoice_total', 'invoice_balance']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'invoice_status': forms.TextInput(attrs={'class': 'form-control'}),
            'observation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Peso, Tamaño, piedra natural?, diamantes de laboratorio, etc.'}),
            'additional_notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Anillo como parte de pago?, etc.'}),
            'invoice_total': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_balance': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InvoiceForItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceForItem
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'additional_notes', 'invoice_status', 'observation', 'invoice_total', 'invoice_balance', 'items']
        labels = {
            'client': 'Cliente',
            'invoice_number': 'Número de Factura',
            'invoice_type': 'Tipo de Factura',
            'invoice_date': 'Fecha de Factura',
            'invoice_status': 'Estado de Factura',
            'observation': 'Observación',
            'invoice_total': 'Total de Factura',
            'invoice_balance': 'Balance de Factura',
            'items': 'Items',
            'additional_notes': 'Notas Adicionales',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control', 'value': 'Factura de Producto', 'readonly': True}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'invoice_status': forms.TextInput(attrs={'class': 'form-control'}),
            'observation': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_total': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_balance': forms.TextInput(attrs={'class': 'form-control'}),
            'items': forms.SelectMultiple(attrs={
                'class': 'form-control select2',  # Add select2 class here
                'multiple': 'multiple'
            }),
            'additional_notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Anillo como parte de pago?, etc.'}),
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

class InvoiceForCustomizedForm(InvoiceForm):
    class Meta:
        model = InvoiceForCustomized
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'invoice_status', 'description', 'observation','additional_notes', 'invoice_total', 'invoice_balance']
        labels = {
            'client': 'Cliente',
            'invoice_number': 'Número de Factura',
            'invoice_type': 'Tipo de Factura',
            'invoice_date': 'Fecha de Factura',
            'invoice_status': 'Estado de Factura',
            'description': 'Descripción',
            'observation': 'Observación',
            'invoice_total': 'Total de Factura',
            'invoice_balance': 'Balance de Factura',
            'additional_notes': 'Notas Adicionales',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control', 'value': 'Factura de Joyas a medida', 'readonly': True}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'invoice_status': forms.TextInput(attrs={'class': 'form-control' ,'readonly': True}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Peso, Tamaño, piedra natural?, diamantes de laboratorio, etc.'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Anillo como parte de pago?, etc.'}),
            'invoice_total': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_balance': forms.TextInput(attrs={'class': 'form-control'}),
        }






