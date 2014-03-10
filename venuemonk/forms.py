from django.forms import ModelForm
from django import forms
from venuemonk.models import *
class venuemonkForm(forms.ModelForm):
        class Meta:
                model = VenueList
		fields = ('name','address',)			
        def clean(self):
                if self.cleaned_data.get('name')=="":
                        raise forms.ValidationError('No name!')
                return self.cleaned_data
