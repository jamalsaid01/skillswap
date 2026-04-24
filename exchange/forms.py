from django import forms
from .models import ExchangeRequest

class ExchangeRequestForm(forms.ModelForm):
    class Meta:
        model = ExchangeRequest
        fields = ['receiver', 'skill_offered', 'skill_requested']