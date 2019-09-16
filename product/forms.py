from django import forms
from django.forms import ModelForm
from product.models import PRODUCT_TYPE, Measure, Product


# class ProductForms(ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"


class ProductForms(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={
            'class': 'form-control',
        }
    ))
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    purchase_price = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    sales_price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    product_type = forms.ChoiceField(choices=PRODUCT_TYPE, widget=forms.Select(attrs={'class': 'form-control'}))
    measure = forms.ModelChoiceField(queryset=Measure.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'image', 'quantity', 'purchase_price', 'sales_price', 'product_type', 'measure']