from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    # path('signup',signup,name='signup'),
    path('login',LoginView.as_view(),name='login'),
    path('',include('django.contrib.auth.urls')),
]