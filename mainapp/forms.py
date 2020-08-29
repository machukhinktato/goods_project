from django import forms
from .models import GoodsItems


class GoodsForm(forms.Form):
    name = forms.CharField(max_length=64)
    price = forms.CharField(max_length=64)

    def clean_name(self):
        new_name = self.cleaned_data['name'].lower()
        return new_name
    # class Meta:
    #     model = GoodsItems
    #     fields = ['name', 'price']
    #
    #     widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'price': forms.TextInput(attrs={'class': 'form-control'}),
    #     }
