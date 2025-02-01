from django import forms
from .models import User

class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(min_value=18, required=True)
