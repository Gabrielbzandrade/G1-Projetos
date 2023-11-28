from django import forms
from .models import Calendario

class CalendarioForm(forms.ModelForm):
    class Meta:
        model = Calendario
        fields = ['data', 'evento']

class ExcluirPerfilForm(forms.Form):
    nome = forms.CharField(max_length=255, required=True)