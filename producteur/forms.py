from django import forms
from marketPlace.models import Producteurs,RefMetier
from django.forms.utils import ErrorList


        
class FicheProducteurForm(forms.ModelForm):
    required_css_class = 'required'
    def __init__(self, *args, **kwargs):
        readOnlyField = kwargs.pop('readOnlyField')
 
        super(FicheProducteurForm, self).__init__(*args, **kwargs)
        


        self.fields['nom'] = forms.CharField(
            label='Nom',
            label_suffix='*',
           
            widget=forms.TextInput(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'placeholder':'Votre nom',
                            
                                        }),
            

        )


        self.fields['raison_social'] = forms.CharField(
            label='Raison social',
            widget=forms.TextInput(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                            'placeholder':'(Facultatif)'}),
            required=False
        )

        CHOICES = [('1', 'First'), ('2', 'Second')]
        self.fields['metier'] = forms.ChoiceField(
            label='Métier',
            widget=forms.Select(attrs={'class': 'form-control',
                                            'disabled':readOnlyField,
                                        'style':'min-width:42%'
                                         }),
            choices=[(rf_choix.id,rf_choix.label) for rf_choix in RefMetier.objects.exclude(id=1)],
            required=False,

        )



    class Meta:
        model = Producteurs
        fields = ["nom","photo","raison_social","num_siren","description","num_telephone_fix",'num_telephone_portable','metier']

f = FicheProducteurForm(readOnlyField='True',auto_id=False)


#for e in f:
#    print(e.label)
#    print(e.field.__dict__)
#    print(e.field.label_suffix)
#    print('***************************************************************')


   # metier = models.ForeignKey('RefMetier', models.DO_NOTHING)
   # adresse = models.ForeignKey(Adresses, models.DO_NOTHING)
  #  date_fin_id = models.IntegerField(blank=True, null=True)

class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="errorMessage">%s</p>' % e for e in self])