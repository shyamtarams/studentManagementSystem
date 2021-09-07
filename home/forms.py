from django import forms
from .models import *


class studentRegisterForm(forms.ModelForm):
    name=forms.CharField(max_length=254)
   
    
    class Meta:
        model=Product
        fields = ('name')

