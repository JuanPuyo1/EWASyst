from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'document_type', 'document_number', 'email', 'address']
        labels = {
            'name': 'Nombre',
            'phone': 'Telefono',
            'email': 'Email',
            'address': 'Direccion',
            'document_type': 'Tipo de Documento',
            'document_number': 'Numero de Documento',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'form-control'}),
            'document_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

