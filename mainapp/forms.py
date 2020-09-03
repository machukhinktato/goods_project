from django import forms
from .models import GoodsItems
from django.core.exceptions import ValidationError


class GoodsForm(forms.ModelForm):

    class Meta:
        model = GoodsItems
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GoodsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        return self.cleaned_data['name'].lower()