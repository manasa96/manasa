from django import forms

from .models import *
from django.contrib.auth.models import User 

class bssForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
	model = bss
	fields = ["first_name","last_name","password","age","city","occupation"]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password','email')

