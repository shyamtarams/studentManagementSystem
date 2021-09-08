from django import forms
from .models import *
from accounts.models import myUser


class studentRegisterForm(forms.ModelForm):
    name=forms.CharField(max_length=254)
    contact =forms.CharField(max_length=15)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    status = forms.CharField(max_length=20)
    rule = forms.CharField(max_length=20)
    # password1=forms.CharField(max_length=50)
    # password2=forms.CharField(max_length=50)
    class Meta:
        model=myUser
        fields = ('name','email','username','contact','status','rule','password')

