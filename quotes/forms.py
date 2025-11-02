from django import forms
from .models import Quote
from dal_select2.widgets import ModelSelect2
from clients.models import Client
from django.utils import timezone
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['client', 'quote_number', 'quote_quantity', 'quote_product_type', 'quote_date', 'quote_value', 'quote_total', 
                  'quote_description', 'quote_additional_notes', 'quote_discount', 'quote_discount_description']
        labels = {
            'client': 'Cliente de la Cotización',
            'quote_number': 'Número de Cotización',
            'quote_quantity': 'Cantidad',
            'quote_product_type': 'Tipo de Producto',
            'quote_date': 'Fecha de Cotización',
            'quote_value': 'Valor',
            'quote_total': 'Total',
            'quote_description': 'Descripción',
            'quote_additional_notes': 'Notas Adicionales',
            'quote_discount': 'Valor del abono',
            'quote_discount_description': 'Descripción del abono',
        }
        widgets = {
            'quote_number': forms.TextInput(attrs={'type': 'text', 'readonly': True}),
            'quote_quantity': forms.NumberInput(attrs={'type': 'number'}),
            'client': ModelSelect2(
                url='clients:clients_autocomplete',
                attrs={
                    'data-placeholder': 'Buscar cliente por nombre...',
                    'data-minimum-input-length': 1,
                }
            ),
            'quote_product_type': forms.Select(attrs={'type': 'select'}),
            'quote_date': forms.DateInput(attrs={'type': 'date'}),
            'quote_value': forms.NumberInput(attrs={'type': 'number', 'localize': True}),
            'quote_total': forms.NumberInput(attrs={'type': 'number', 'localize': True}),
            'quote_description': forms.Textarea(),
            'quote_additional_notes': forms.Textarea(attrs={'rows': 4}),
            'quote_discount': forms.NumberInput(attrs={'type': 'number', 'localize': True}),
            'quote_discount_description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        time_now = timezone.now().date()
        time_now = time_now.strftime('%Y-%m-%d')
        self.fields['quote_date'].initial = time_now 



