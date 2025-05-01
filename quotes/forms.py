from django import forms
from .models import Quote



class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['client', 'quote_number', 'quote_quantity', 'quote_product_type', 'quote_date', 'quote_total', 'quote_description', 'quote_additional_notes']
        labels = {
            'client': 'Cliente de la Cotización',
            'quote_number': 'Número de Cotización',
            'quote_quantity': 'Cantidad',
            'quote_product_type': 'Tipo de Producto',
            'quote_date': 'Fecha de Cotización',
            'quote_total': 'Total',
            'quote_description': 'Descripción',
            'quote_additional_notes': 'Notas Adicionales',
            
        }
        widgets = {
            'quote_number': forms.TextInput(attrs={'type': 'text', 'readonly': True}),
            'quote_quantity': forms.NumberInput(attrs={'type': 'number'}),
            'client': forms.Select(attrs={'type': 'select'}),
            'quote_product_type': forms.Select(attrs={'type': 'select'}),
            'quote_date': forms.DateInput(attrs={'type': 'date'}),
            'quote_total': forms.NumberInput(attrs={'type': 'number', 'localize': True}),
            'quote_description': forms.Textarea(),
            'quote_additional_notes': forms.Textarea(attrs={'rows': 4}),
        }



