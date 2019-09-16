from django.forms import ModelForm
from django import forms
from customers.models import Customer


class CustomerModelForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    mobile_number = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    billing_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    shipping_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Customer
        fields = ['name', 'mobile_number', 'email', 'address', 'billing_address', 'shipping_address']
