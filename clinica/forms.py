from django import forms
from .models import Paciente


class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['historial_medico']
