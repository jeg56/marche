from django import forms
from django.db import models
from marketPlace.models import Producteurs

        
class ProducteurForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        readOnlyField = kwargs.pop('readOnlyField') 
        producteur = kwargs.pop('producteur')
        RefMetier= kwargs.pop('refMetier')
 
        super(ProducteurForm, self).__init__(*args, **kwargs)
        
        # --------------------------------------------------------------------------------------------------------------------------------------
        # Nom
        # --------------------------------------------------------------------------------------------------------------------------------------
        if producteur.nom:
            self.fields['nom'] = forms.CharField(
                label='Nom',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'value': producteur.nom,
                                                'style':'color:black',
                                                'placeholder':'Entrez votre nom',
                                            }),
                required=False
            )
        else:
            self.fields['nom'] = forms.CharField(
                label='Nom',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'style':'color:black',
                                                'placeholder':'Entrez votre nom',
                                            }),
                required=False
            )

        # --------------------------------------------------------------------------------------------------------------------------------------
        # raison_social
        # --------------------------------------------------------------------------------------------------------------------------------------
        if producteur.raison_social:
            self.fields['raison_social'] = forms.CharField(
                label='Raison social',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'value': producteur.raison_social,
                                                'style':'color:black',
                                                'placeholder':'Entrez votre raison social',
                                            }),
                required=False
            )
        else:
            self.fields['raison_social'] = forms.CharField(
                label='Raison social',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'style':'color:black',
                                                'placeholder':'Entrez votre raison social',
                                            }),
                required=False
            )

        # --------------------------------------------------------------------------------------------------------------------------------------
        # num_siren
        # --------------------------------------------------------------------------------------------------------------------------------------
        if producteur.num_siren:
            self.fields['num_siren'] = forms.CharField(
                label='Numéro de siren',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'value': producteur.num_siren,
                                                'style':'color:black',
                                                'placeholder':'Entrez votre numéro de siren',
                                            }),
                required=False
            )
        else:
            self.fields['num_siren'] = forms.CharField(
            label='Numéro de siren',
            widget=forms.TextInput(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'style':'color:black',
                                            'placeholder':'Entrez votre numéro de siren',
                                        }),
            required=False
        )

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Description
        # --------------------------------------------------------------------------------------------------------------------------------------
        if producteur.description:
            self.fields['description'] = forms.CharField(
                label='Description',
                widget=forms.Textarea(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'style':'color:black',
                                                'placeholder':'Décrivez qui vous êtes ce que vous faisez ... ',
                        
                                            }),
                initial= producteur.description,
                required=False
            )
        else:
            self.fields['description'] = forms.CharField(
                label='Description',
                widget=forms.Textarea(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'style':'color:black',
                                                'placeholder':'Décrivez qui vous êtes ce que vous faisez ... ',
                                      
                                            }),
                required=False
            )
        # --------------------------------------------------------------------------------------------------------------------------------------
        # num_telephone_fix
        # --------------------------------------------------------------------------------------------------------------------------------------
        if producteur.num_telephone_fix:
            self.fields['num_telephone_fix'] = forms.CharField(
                label='Téléphone fixe',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'value': producteur.num_telephone_fix,
                                                'style':'color:black',
                                                'placeholder':'02.00.00.00.00 ',
                                            }),
                required=False
            )
        else:
            self.fields['num_telephone_fix'] = forms.CharField(
                label='Téléphone fixe',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'style':'color:black',
                                                'placeholder':'02.00.00.00.00 ',
                                            }),
                required=False
            )
        # --------------------------------------------------------------------------------------------------------------------------------------
        # num_telephone_portable
        # --------------------------------------------------------------------------------------------------------------------------------------
        if  producteur.num_telephone_portable:
            self.fields['num_telephone_portable'] = forms.CharField(
                label='Téléphone protable',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'value': producteur.num_telephone_portable,
                                                'style':'color:black',
                                                'placeholder':'06.00.00.00.00 ',
                                            }),
                required=False
            )
        else:
            self.fields['num_telephone_portable'] = forms.CharField(
                label='Téléphone protable',
                widget=forms.TextInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'style':'color:black',
                                                'placeholder':'06.00.00.00.00 ',
                                            }),
                required=False
            )
        # --------------------------------------------------------------------------------------------------------------------------------------
        # Métier
        # --------------------------------------------------------------------------------------------------------------------------------------
        self.fields['metier'] = forms.ChoiceField(
            label='Métier',
            widget=forms.Select(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'style':'min-width:42%;color:black'
                                         }),
            choices=[(rf_choix.id,rf_choix.label) for rf_choix in RefMetier],
            initial=producteur.metier_id,
            required=True,
        )
        self.fields['photo'].required = False
    # --------------------------------------------------------------------------------------------------------------------------------------
    # Photo
    # --------------------------------------------------------------------------------------------------------------------------------------
    photo = models.URLField()


    class Meta:
        model = Producteurs
        fields = ["nom","photo","raison_social","num_siren","description","num_telephone_fix",'num_telephone_portable','metier']
        exclude = ['metier']
#f = ProducteurForm(readOnlyField='True',idProducteur=1)


  #for e in f:
  #    print(e.label)
  #    print(e.field.__dict__)
   #   print(e.field.label_suffix)
     # print('***************************************************************')


   # metier = models.ForeignKey('RefMetier', models.DO_NOTHING)
   # adresse = models.ForeignKey(Adresses, models.DO_NOTHING)
  #  date_fin_id = models.IntegerField(blank=True, null=True)

