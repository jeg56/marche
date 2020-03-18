
from django import forms
from django.db import models
from marketPlace.models import Produits
from django.forms.utils import ErrorList
from collections import OrderedDict

class ProduitsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        readOnlyField = kwargs.pop('readOnlyField')
        refFamille = kwargs.pop('refFamille')
        refCategorie = kwargs.pop('refCategorie')
        produit= kwargs.pop('produit')

        super(ProduitsForm, self).__init__(*args, **kwargs)

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Famille de produit
        # --------------------------------------------------------------------------------------------------------------------------------------
        self.fields['famille'] = forms.ChoiceField(
            label='Famille du produit',
            widget=forms.Select(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'style':'min-width:42%;color:black',
                                            'id':'id_famille',
                                            'onfocus':'searchFamille()',
                                            'onchange': 'searchCategorie()'
                                         }),
       
           # initial=Producteurs.objects.get(pk=idProducteur).metier_id,
            required=True,
        )

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Catégorie de produit
        # --------------------------------------------------------------------------------------------------------------------------------------
        self.fields['categorie'] = forms.ChoiceField(
            label='Catégorie du produit',
            widget=forms.Select(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'style':'min-width:42%;color:black;',
                                            'onfocus':'searchCategorie()',
                                            'placeholder':"Entrer votre produit"       
                                         }),
          
     
            required=True,
        )
     

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Produit
        # --------------------------------------------------------------------------------------------------------------------------------------
        """  self.fields['nom'] = forms.ChoiceField(
            label='Produit',
            widget=forms.Select(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'style':'min-width:42%;color:black',
                                            'id':'id_produit',
                                         }),
            
            required=True,
        )
            """
        self.order_fields(['famille','categorie'])

    
    class Meta:
        model = Produits
     
        exclude=('nom','photo')

    









class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
       
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="errorMessage">%s</p>' % e for e in self])