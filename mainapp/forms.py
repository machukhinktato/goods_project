from django import forms
from .models import GoodsItems


class GoodsForm(forms.ModelForm):
    class Meta:
        model = GoodsItems
        fields = ['товар', 'цена']

        widgets = {
            'товар': forms.TextInput(attrs={'class': 'form-control'}),
            'цена': forms.TextInput(attrs={'class': 'form-control'}),
        }
