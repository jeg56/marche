from django import forms
from marketPlace.models import Connexions,Producteurs
from django.forms.utils import ErrorList

class ConnexionProducteurForm(forms.ModelForm):
    repassword = forms.CharField()
    class Meta:
        model = Connexions
        fields = ["identifiant", "password","email","opt_in"]
        widgets = {
            'identifiant': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'opt_in': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
        
class IdentificationProducteurForm(forms.ModelForm):
    class Meta:
        model = Connexions
        fields = ["identifiant", "password"]
        widgets = {
            'identifiant': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="errorMessage">%s</p>' % e for e in self])