
from django import forms
from .models import Invoice
from datetime import datetime, timedelta
from dal_select2.widgets import ModelSelect2
from django.utils import timezone

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'invoice_number', 'invoice_type', 'invoice_date', 'invoice_status', 'observation', 'invoice_quantity', 'additional_notes', 'invoice_total', 'invoice_balance', 'invoice_discount', 'invoice_discount_description']
        labels = {
            'client': 'Cliente',
            'invoice_number': 'Número de Factura',
            'invoice_type': 'Tipo de Factura',
            'invoice_date': 'Fecha de Factura',
            'invoice_status': 'Estado de Factura',
            'observation': 'Descripción de la factura',
            'invoice_quantity': 'Cantidad',
            'additional_notes': 'Notas Adicionales',
            'invoice_total': 'Total de Factura',
            'invoice_balance': 'Abono de Factura',
            'invoice_discount': 'Valor del descuento NOTA: El valor del descuento se aplica al total de la factura',
            'invoice_discount_description': 'Descripción del descuento NOTA: La descripción del descuento se muestra en la factura',
        }
        widgets = {
            'client': ModelSelect2(
                url='clients:clients_autocomplete',
                attrs={
                    'data-placeholder': 'Buscar cliente por nombre...',
                    'data-minimum-input-length': 1,
                }
            ),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'invoice_status': forms.Select(attrs={'class': 'form-control', 'id': 'invoice_status_id'}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tipo de anillo, talla, material, peso, etc.'}),
            'invoice_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Anillo como parte de pago?, etc.'}),
            'invoice_total': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_discount': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_discount_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del descuento, pago de primera compra, etc.', 'rows': 4}), 
            'invoice_balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de abono de la factura'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        time_now = timezone.now().date()
        time_now = time_now.strftime('%Y-%m-%d')
        self.fields['invoice_date'].initial = time_now

