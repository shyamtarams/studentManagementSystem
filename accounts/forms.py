from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import myUser

class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = myUser
        field = "__all__"


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
