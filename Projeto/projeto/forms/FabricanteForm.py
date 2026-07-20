from django.forms import ModelForm
from django import forms
from projeto.models.Fabricante import Fabricante

class FabricanteForm(ModelForm):
    class Meta:
        model = Fabricante
        fields = [
            'Fabricante'
        ]

        widgets = {
            'Fabricante': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }