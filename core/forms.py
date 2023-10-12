from django import forms
from .models import Personal, Solicitud, ReporteVentas

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
        
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        
class ReporteForm(forms.ModelForm):
    class Meta:
        model = ReporteVentas
        fields = '__all__'
        widgets = {
            'mes': forms.TextInput(attrs={'class': 'form-control'})
        }