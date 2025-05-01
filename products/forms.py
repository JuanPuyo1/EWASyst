from django import forms
from .models import Ring, Stone, ChainOrBracelet

class RingForm(forms.ModelForm):
    class Meta:
        model = Ring
        fields = '__all__'

        labels = {
            'jewellery_name': 'Nombre',
            'jewellery_quantity': 'Cantidad',
            'certificate': 'Certificado',
            'ring_description': 'Descripción detallada del Anillo',
            'ring_size': 'Tamaño del Anillo',
            'ring_type': 'Tipo de Anillo',
            'ring_quality': 'Calidad del Anillo',
            'ring_weight': 'Peso del Anillo',
            'synthetic_stone': 'Diamantes de laboratorio?',
        }

        widgets = {
            'jewellery_name': forms.TextInput(attrs={'class': 'form-control', 'value': 'Anillo', 'readonly': True}),
            'jewellery_quantity': forms.TextInput(attrs={'class': 'form-control', 'value': '1', 'readonly': True}),
            'certificate': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ring_description': forms.TextInput(attrs={'class': 'form-control'}),
            'ring_size': forms.TextInput(attrs={'class': 'form-control'}),
            'ring_type': forms.Select(attrs={'class': 'form-control'}),
            'ring_quality': forms.Select(attrs={'class': 'form-control'}),
            'ring_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'synthetic_stone': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class ChainOrBraceletForm(forms.ModelForm):
    class Meta:
        model = ChainOrBracelet
        fields = '__all__'
        labels = {
            'jewellery_name': 'Nombre del Accesorio',
            'jewellery_quantity': 'Cantidad del Accesorio',
            'certificate': 'Certificado',
            'chain_or_bracelet_weight': 'Peso del Accesorio',
            'chain_or_bracelet_quality': 'Calidad del Accesorio',
            'long': 'Longitud del Accesorio',
            'fabric': 'Material del Accesorio',
        }
        widgets = {
            'jewellery_name': forms.TextInput(attrs={'class': 'form-control'}),
            'jewellery_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'certificate': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'chain_or_bracelet_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'chain_or_bracelet_quality': forms.TextInput(attrs={'class': 'form-control'}),
            'long': forms.TextInput(attrs={'class': 'form-control'}),
            'fabric': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StoneForm(forms.ModelForm):
    class Meta:
        model = Stone
        fields = '__all__'
        labels = {
            'stone_description': 'Descripción detallada de la Piedra',
            'stone_color': 'Color de la Piedra',
            'stone_clarity': 'Claridad de la Piedra',
            'stone_carat': 'Carat de la Piedra',
        }
        widgets = {
            'stone_description': forms.TextInput(attrs={'class': 'form-control'}),
            'stone_color': forms.TextInput(attrs={'class': 'form-control'}),
            'stone_clarity': forms.TextInput(attrs={'class': 'form-control'}),
            'stone_carat': forms.TextInput(attrs={'class': 'form-control'}),
        }