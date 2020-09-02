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

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'price': forms.TextInput(attrs={'class': 'form-control'}),
        # }


    # def clean_name(self):
    #     new_name = self.cleaned_data['name'].lower()
    #
    #     # if new_name == 'create':
    #     #     raise ValidationError('slug may not be "Create"')
    #     if GoodsItems.objects.filter(name__iexact=new_name).count():
    #         raise ValidationError(
    #             f'Slug must be a unique. We have a slug "{new_name}" already'
    #         )
    #     return new_name