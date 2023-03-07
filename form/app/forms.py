from django import forms
from .models import Student


class Studentregistration(forms.Form):
    name=forms.CharField()
    section=forms.CharField()
    contact=forms.IntegerField()
    email=forms.EmailField()
    school=forms.CharField()