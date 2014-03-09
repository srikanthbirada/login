from django.forms import ModelForm
from django import forms

class AddVenue(forms.Form):
	name = forms.CharField(max_length=20)
	address = forms.CharField(max_length=20)

class AddOwner(forms.Form):
	name = forms.CharField(max_length=20)
	mobile_number = forms.CharField(max_length=10)
	email_id = forms.EmailField()
