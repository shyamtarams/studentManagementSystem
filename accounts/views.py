from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from random import randint
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

#import form
from .forms import SignUpForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
