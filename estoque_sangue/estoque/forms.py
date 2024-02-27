# No arquivo forms.py
from django import forms
from .models import EstoqueSangue

class EstoqueSangueForm(forms.ModelForm):
    class Meta:
        model = EstoqueSangue
        fields = '__all__'
        widgets = {
            'hemocentro': forms.Select(attrs={'class': 'form-control'}),
        }
