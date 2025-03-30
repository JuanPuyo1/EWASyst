from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'description', 'price', 'stock']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'stock': 'Stock'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
        }
        


