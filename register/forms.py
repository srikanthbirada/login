from django.forms import ModelForm
from django import forms

from register.models import *

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)
