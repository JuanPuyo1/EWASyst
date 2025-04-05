
from django import forms
from .models import Invoice, InvoiceForItem, InvoiceForMaintenance, InvoiceForStone, Stone, Ring, ChainOrBracelet



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
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_type': forms.TextInput(attrs={'class': 'form-control'}),
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

class StoneForm(forms.ModelForm):
    class Meta:
        model = Stone
        fields = [ 'stone_name', 'stone_color', 'stone_clarity', 'stone_carat']
        labels = {
            'stone_name': 'Nombre detallado de la Piedra',
            'stone_color': 'Color de la Piedra',
            'stone_clarity': 'Claridad de la Piedra',
            'stone_carat': 'Carat de la Piedra',
        }
        widgets = {
            'stone_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stone_color': forms.TextInput(attrs={'class': 'form-control'}),
            'stone_clarity': forms.TextInput(attrs={'class': 'form-control'}),
            'stone_carat': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class RingForm(forms.ModelForm):
#     class Meta:
#         model = Ring
#         fields = ['ring_size', 'ring_type', 'ring_quality', 'ring_weight', 'diamond', 'synthetic_stone']
#         labels = {
#             'ring_size': 'Tamaño del Anillo',
#             'ring_type': 'Tipo de Anillo',
#             'ring_quality': 'Calidad del Anillo',
#             'ring_weight': 'Peso del Anillo',
#             'diamond': 'Diamante',
#             'synthetic_stone': 'Piedra Sintética',
#         }
#         widgets = {
#             'ring_size': forms.TextInput(attrs={'class': 'form-control'}),
#             'ring_type': forms.TextInput(attrs={'class': 'form-control'}),
#             'ring_quality': forms.TextInput(attrs={'class': 'form-control'}),
#             'ring_weight': forms.TextInput(attrs={'class': 'form-control'}),
#             'diamond': forms.Select(attrs={'class': 'form-control'}),
#             'synthetic_stone': forms.CheckboxInput(attrs={'class': 'form-control'}),
#         }



# class ChainOrBraceletForm(forms.ModelForm):
#     class Meta:
#         model = ChainOrBracelet
#         fields = ['chain_or_bracelet_type', 'chain_or_bracelet_quality', 'chain_or_bracelet_weight', 'chain_or_bracelet_length']
#         labels = {
#             'chain_or_bracelet_type': 'Tipo de Cadena o Brazalete',
#             'chain_or_bracelet_quality': 'Calidad de la Cadena o Brazalete',
#             'chain_or_bracelet_weight': 'Peso de la Cadena o Brazalete',
#             'chain_or_bracelet_length': 'Longitud de la Cadena o Brazalete',
#         }
#         widgets = {
#             'chain_or_bracelet_type': forms.TextInput(attrs={'class': 'form-control'}),
#             'chain_or_bracelet_quality': forms.TextInput(attrs={'class': 'form-control'}),
#             'chain_or_bracelet_weight': forms.TextInput(attrs={'class': 'form-control'}),
#             'chain_or_bracelet_length': forms.TextInput(attrs={'class': 'form-control'}),
#         }





