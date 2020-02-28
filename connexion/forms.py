from django import forms
from marketPlace.models import Connexions

class ConnexionProducteurForm(forms.ModelForm):
    class Meta:
        model = Connexions
        fields = ["identifiant", "password","email","opt_in"]
        widgets = {
            'identifiant': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'opt_in': forms.NumberInput(attrs={'class': 'form-control'}),
        }