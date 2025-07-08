
from django import forms
from .models import Invoice
from datetime import datetime, timedelta

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'invoice_status', 'observation', 'invoice_quantity', 'additional_notes', 'invoice_total', 'invoice_balance']
        labels = {
            'client': 'Cliente',
            'invoice_number': 'Número de Factura',
            'invoice_type': 'Tipo de Factura',
            'invoice_date': 'Fecha de Factura',
            'invoice_status': 'Estado de Factura',
            'observation': 'Observación',
            'invoice_quantity': 'Cantidad',
            'additional_notes': 'Notas Adicionales',
            'invoice_total': 'Total de Factura',
            'invoice_balance': 'Balance de Factura',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'invoice_status': forms.Select(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={'class': 'form-control'}),
            'invoice_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Anillo como parte de pago?, etc.'}),
            'invoice_total': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_balance': forms.TextInput(attrs={'class': 'form-control'}),
        }

