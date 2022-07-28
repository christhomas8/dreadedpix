from django import forms
from .models import Inquiry

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField()
    phone = forms.CharField(max_length=15,required="false")
    date = forms.CharField(max_length=50)

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('name','email','phone','date')