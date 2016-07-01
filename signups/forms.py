from django import forms

from .models import *

"""class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
"""
class CustomerForm(forms.ModelForm):
    class Meta:
	model = Customer
	fields = ["name","roll","age"]
