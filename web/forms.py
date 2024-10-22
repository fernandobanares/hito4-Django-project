from django import forms
from .models import Contact

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['customer_name', 'customer_email', 'message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
