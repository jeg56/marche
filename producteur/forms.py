from django import forms
from marketPlace.models import Producteurs
from django.forms.utils import ErrorList


class FicheProducteurForm(forms.ModelForm):
    class Meta:
        model = Producteurs
        fields = ["nom"]



class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="errorMessage">%s</p>' % e for e in self])