from django import forms
from django.db import models
from marketPlace.models import Marches,RefManifestation,RefFrequence,RefHoraire,RefJoursSemaine,JourMarche


class MarchesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        readOnlyField = kwargs.pop('readOnlyField')
        Marches = kwargs.pop('marche')
        super(MarchesForm, self).__init__(*args, **kwargs)

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Nom
        # --------------------------------------------------------------------------------------------------------------------------------------

        self.fields['nom'] = forms.CharField(
            label='Nom du marché',
            widget=forms.TextInput(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'value': Marches.nom,
                                            'style':'color:black',
                                            'placeholder':'Entrez le nom du marché',
                                        }),
            required=True
        )


  
        # --------------------------------------------------------------------------------------------------------------------------------------
        # Manifestation
        # --------------------------------------------------------------------------------------------------------------------------------------
        self.fields['manifestation'] = forms.ChoiceField(
            label='Type de manifestation',
            widget=forms.Select(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'style':'min-width:42%;color:black'
                                         }),
            choices=[(rf_choix.id,rf_choix.label) for rf_choix in RefManifestation.objects.all()],
            initial=Marches.manifestation_id,
            required=True,
        )
        

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Nbre d'exposant
        # --------------------------------------------------------------------------------------------------------------------------------------
        if Marches.nb_exposant:
            self.fields['nb_exposant'] = forms.IntegerField(
                label='Nombre d\'exposant',
                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'value': Marches.nb_exposant,
                                                'style':'color:black',
                                                'initial': 0,
                                                'min_value':0,
                                            }),
                required=False
            )
        else:
            self.fields['nb_exposant'] = forms.IntegerField(
                label='Nombre d\'exposant',
                widget=forms.NumberInput(attrs={'class': 'form-control',
                                                'disabled':readOnlyField,
                                                'style':'color:black',
                                                'initial': 0,
                                                'min_value':0,
                                            }),
                required=False
            )




        # --------------------------------------------------------------------------------------------------------------------------------------
        # Photo
        # --------------------------------------------------------------------------------------------------------------------------------------
        self.fields['photo'].required = False


    class Meta:
        model = Marches
        fields = ['nom','photo']




class JourMarcheForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        print('-----------------------------------------')
        print(data.get('Mercredi', None))
        print('-----------------------------------------')
        if data.get('Mercredi', None):
            return data
        else:
            raise forms.ValidationError('Provide either a date and time or a timestamp')
    class Meta:
        model = JourMarche
        fields = ['heure_debut','heure_fin']
