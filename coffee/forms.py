# forms.py
from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'payment_method', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your phone number'}),
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your shipping address'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Any special instructions?'}),
        }