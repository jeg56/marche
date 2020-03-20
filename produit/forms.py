
from django import forms
from django.db import models
from marketPlace.models import Produits,RefCategorie
from django.forms.utils import ErrorList
from collections import OrderedDict

class ProduitsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProduitsForm, self).__init__(*args, **kwargs)

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Categorie 
        # --------------------------------------------------------------------------------------------------------------------------------------
        self.fields['categorie'] = forms.ChoiceField(
            label='Catégorie du produit',
            choices=[(rf_choix.id,rf_choix.label) for rf_choix in RefCategorie.objects.all()],
            required=True,
  
        )

    nom = forms.CharField(label='Nom du produit')

    class Meta:
        model = Produits
        fields = ["nom"]
       

class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
       
        if not self: return ''
        return  ''.join(['%s' % e for e in self])