
from django import forms
from django.db import models
from marketPlace.models import Adresses,Communes
from django.forms.utils import ErrorList





class AdressesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        readOnlyField = kwargs.pop('readOnlyField')
        Adresses = kwargs.pop('adresse')

        super(AdressesForm, self).__init__(*args, **kwargs)

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Adresses
        # --------------------------------------------------------------------------------------------------------------------------------------
        if Adresses:
            if Adresses.adresse:
                self.fields['adresse'] = forms.CharField(
                    label='Adresse',
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'disabled':readOnlyField,
                                                    'value': Adresses.adresse,
                                                    'style':'color:black',
                                                    'placeholder':'Entrez votre adresse',
                                                }),
                    required=False
                )
            else:
                self.fields['adresse'] = forms.CharField(
                    label='Adresse',
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'disabled':readOnlyField,
                                                    'style':'color:black',
                                                    'placeholder':'Entrez votre adresse',
                                                }),
                    required=False
                )

            # --------------------------------------------------------------------------------------------------------------------------------------
            # Code postal
            # --------------------------------------------------------------------------------------------------------------------------------------
            if Adresses.cp:
                self.fields['cp'] = forms.CharField(
                    label='Code postal',
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'disabled':readOnlyField,
                                                    'value': Adresses.cp,
                                                    'style':'color:black',
                                                     'onkeyup':'searchCP()',
                                                     'autocomplete':'on',
                                                    'placeholder':'Entrez votre code postal',
                                                }),
                    required=False
                )
            else:
                self.fields['cp'] = forms.CharField(
                    label='Code postal',
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'disabled':readOnlyField,
                                                    'style':'color:black',
                                                    'onkeyup':'searchCP()',
                                                    'autocomplete':'on',
                                                    'placeholder':'Entrez votre code postal',
                                                }),
                    required=False
                )

            # --------------------------------------------------------------------------------------------------------------------------------------
            # Ville
            # --------------------------------------------------------------------------------------------------------------------------------------
            if Adresses.ville:
                self.fields['ville'] = forms.CharField(
                    label='Ville',
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'disabled':readOnlyField,
                                                    'value': Adresses.ville,
                                                    'onkeyup':'searchVille()',
                                                    'style':'color:black',
                                                    'autocomplete':'on',
                                                    'placeholder':'Entrez votre ville',
                                                }),
                    required=False
                )
            else:
                self.fields['ville'] = forms.CharField(
                    label='Ville',
                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'disabled':readOnlyField,
                                                    'onkeyup':'searchVille()',
                                                    'style':'color:black',
                                                    'autocomplete':'on',
                                                    'placeholder':'Entrez votre ville',
                                                }),
                    required=False
                )

                          



    class Meta:
        model = Adresses
        fields = ['adresse']









class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
       
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="errorMessage">%s</p>' % e for e in self])