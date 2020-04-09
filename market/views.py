# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from marketPlace.models import Marches,Adresses,RefManifestation,RefFrequence,RefHoraire,Communes,JourMarche
from marketPlace.forms import ParagraphErrorList,AdressesForm 
from django.shortcuts import render,get_object_or_404
from .forms import MarchesForm
from django.db import transaction
from marketPlace.fonctionnalites import getLocalisation
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django import template

register = template.Library()
#@login_required(login_url='connexion:identification')
@transaction.atomic
@register.filter
def fiche_marche(request,id=None):
    jourMarche=None
    if request.path=='/market/add/':
        marche=Marches()
        adresse=Adresses()
        marche.adresse=adresse
        marche.id=0
        jourMarche=JourMarche.objects.filter(id=0)

    elif id=='0':
        marche=Marches()
        adresse=Adresses()
        marche.adresse=adresse
        jourMarche=JourMarche.objects.filter(id=0)
        marche.id=0
    else:
        marche=get_object_or_404(Marches,pk=id)
        adresse= marche.adresse
        jourMarche=JourMarche.objects.filter(ref_marche_id=id)

      
    errorsDateMarche={}
    context = {
        'title': 'Infos sur le marché',
    }
    listHoraire=RefHoraire.objects.all()
    context['horaireJson']=listHoraire.values('id','label')

    result = []

    # on regarde si le producteur est identifié ( loggué )
    identifie=False
    readOnlyField=True

    
    if 'id' in request.session:
        readOnlyField=False
        identifie=True
        context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche)  
        context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)  
    else:
        context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche)   
        context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)    

    
    if request.method == 'POST':
        formMarche=MarchesForm(readOnlyField=readOnlyField,marche=marche,data=request.POST, error_class=ParagraphErrorList)
        formAdresse=AdressesForm(readOnlyField=readOnlyField,adresse=adresse, data=request.POST, error_class=ParagraphErrorList)
      


        if formAdresse.is_valid() and formMarche.is_valid():
            adrs = formAdresse.cleaned_data['adresse']
            cp = formAdresse.cleaned_data['cp']
            ville = formAdresse.cleaned_data['ville']

            if(adresse.adresse!=adrs or adresse.cp!=cp or adresse.ville)!=ville:
                rechercheGeocodage=adrs+' '+cp +' '+ ville
                try:
                    latitude,longitude=getLocalisation.getLocalisation(rechercheGeocodage)
                except:
                    latitude=0
                    longitude=0
                adresse , created = Adresses.objects.get_or_create(adresse=adrs,cp=cp,ville=ville)
                adresse.latitude=latitude
                adresse.longitude=longitude
                adresse.save()
                marche.adresse=adresse

            nom = formMarche.cleaned_data['nom']
            if request.FILES.get('photo'):    
                photo=request.FILES['photo']
                marche.photo = photo

            manifestation = formMarche.cleaned_data['manifestation']
        
            nb_exposant= formMarche.cleaned_data['nb_exposant']

            manifestation=RefManifestation.objects.get(pk=manifestation)
            Lundi=request.POST.get('Lundi')
            LundiSelectDeb=request.POST.get('LundiSelectDeb',None)
            LundiSelectFin=request.POST.get('LundiSelectFin',None)

            Mardi=request.POST.get('Mardi')
            MardiSelectDeb=request.POST.get('MardiSelectDeb',None)
            MardiSelectFin=request.POST.get('MardiSelectFin',None)

            Mercredi=request.POST.get('Mercredi')
            MercrediSelectDeb=request.POST.get('MercrediSelectDeb',None)
            MercrediSelectFin=request.POST.get('MercrediSelectFin',None)

            Jeudi=request.POST.get('Jeudi')
            JeudiSelectDeb=request.POST.get('JeudiSelectDeb',None)
            JeudiSelectFin=request.POST.get('JeudiSelectFin',None)

            Vendredi=request.POST.get('Vendredi')
            VendrediSelectDeb=request.POST.get('VendrediSelectDeb',None)
            VendrediSelectFin=request.POST.get('VendrediSelectFin',None)

            Samedi=request.POST.get('Samedi')
            SamediSelectDeb=request.POST.get('SamediSelectDeb',None)
            SamediSelectFin=request.POST.get('SamediSelectFin',None)

            Dimanche=request.POST.get('Dimanche')
            DimancheSelectDeb=request.POST.get('DimancheSelectDeb',None)
            DimancheSelectFin=request.POST.get('DimancheSelectFin',None)

            jourMarche.delete()
         
            #Cas marche deja créé
            if id!='0':
                marche.nom=nom
                marche.manifestation=manifestation

                marche.nb_exposant=nb_exposant
                marche.historique=('{} maj par {} \n').format(marche.historique,request.session['identifiant']) if marche.historique else ('maj par {} \n').format(request.session['identifiant'])
                marche.save()


                if Lundi==None:
                    pass
                elif Lundi == "on" and LundiSelectDeb and LundiSelectFin and LundiSelectDeb<LundiSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=1,
                                                    heure_debut=listHoraire.get(pk=LundiSelectDeb),
                                                    heure_fin=listHoraire.get(pk=LundiSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Lundi'] = 'Merci de sélectionner une heure de début & de fin cohérente'



                if Mardi==None:
                    pass
                elif Mardi == "on" and MardiSelectDeb and MardiSelectFin and MardiSelectDeb<MardiSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=2,
                                                    heure_debut=listHoraire.get(pk=MardiSelectDeb),
                                                    heure_fin=listHoraire.get(pk=MardiSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Mardi'] = 'Merci de sélectionner une heure de début & de fin cohérente'



                if Mercredi==None:
                    pass
                elif Mercredi == "on" and MercrediSelectDeb and MercrediSelectFin and MercrediSelectDeb < MercrediSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=3,
                                                    heure_debut=listHoraire.get(pk=MercrediSelectDeb),
                                                    heure_fin=listHoraire.get(pk=MercrediSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Mercredi'] = 'Merci de sélectionner une heure de début & de fin cohérente'


                if Jeudi==None:
                    pass
                elif Jeudi == "on" and JeudiSelectDeb and JeudiSelectFin and JeudiSelectDeb < JeudiSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=4,
                                                    heure_debut=listHoraire.get(pk=JeudiSelectDeb),
                                                    heure_fin=listHoraire.get(pk=JeudiSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Jeudi'] = 'Merci de sélectionner une heure de début & de fin cohérente'

                #--------------------------------------------------------------------------------------------
                if Vendredi==None:
                    pass
                elif Vendredi == "on" and VendrediSelectDeb and VendrediSelectFin and VendrediSelectDeb < VendrediSelectFin :
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=5,
                                                    heure_debut=listHoraire.get(pk=VendrediSelectDeb),
                                                    heure_fin=listHoraire.get(pk=VendrediSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Vendredi'] = 'Merci de sélectionner une heure de début & de fin cohérente'

                #--------------------------------------------------------------------------------------------
                if Samedi==None:
                    pass
                elif Samedi == "on" and SamediSelectDeb and SamediSelectFin and SamediSelectDeb < SamediSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=6,
                                                    heure_debut=listHoraire.get(pk=SamediSelectDeb),
                                                    heure_fin=listHoraire.get(pk=SamediSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Samedi'] = 'Merci de sélectionner une heure de début & de fin cohérente'

                if Dimanche==None:
                    pass
                elif Dimanche == "on" and DimancheSelectDeb and DimancheSelectFin and DimancheSelectDeb < DimancheSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=7,
                                                    heure_debut=listHoraire.get(pk=DimancheSelectDeb),
                                                    heure_fin=listHoraire.get(pk=DimancheSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Dimanche'] = 'Merci de sélectionner une heure de début & de fin cohérente'


                
            else: 
                #cas maché a créer               
                marche , created = Marches.objects.get_or_create(nom=nom,
                                                manifestation=manifestation,
                                                nb_exposant=nb_exposant,
                                                adresse=adresse,
                                                date_debut_id=1
                                                )
                marche.save()

                if Lundi==None:
                    pass
                elif Lundi == "on" and LundiSelectDeb and LundiSelectFin and LundiSelectDeb<LundiSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=1,
                                                    heure_debut=listHoraire.get(pk=LundiSelectDeb),
                                                    heure_fin=listHoraire.get(pk=LundiSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Lundi'] = 'Merci de sélectionner une heure de début & de fin cohérente'



                if Mardi==None:
                    pass
                elif Mardi == "on" and MardiSelectDeb and MardiSelectFin and MardiSelectDeb<MardiSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=2,
                                                    heure_debut=listHoraire.get(pk=MardiSelectDeb),
                                                    heure_fin=listHoraire.get(pk=MardiSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Mardi'] = 'Merci de sélectionner une heure de début & de fin cohérente'



                if Mercredi==None:
                    pass
                elif Mercredi == "on" and MercrediSelectDeb and MercrediSelectFin and MercrediSelectDeb < MercrediSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=3,
                                                    heure_debut=listHoraire.get(pk=MercrediSelectDeb),
                                                    heure_fin=listHoraire.get(pk=MercrediSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Mercredi'] = 'Merci de sélectionner une heure de début & de fin cohérente'


                if Jeudi==None:
                    pass
                elif Jeudi == "on" and JeudiSelectDeb and JeudiSelectFin and JeudiSelectDeb < JeudiSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=4,
                                                    heure_debut=listHoraire.get(pk=JeudiSelectDeb),
                                                    heure_fin=listHoraire.get(pk=JeudiSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Jeudi'] = 'Merci de sélectionner une heure de début & de fin cohérente'

                #--------------------------------------------------------------------------------------------
                if Vendredi==None:
                    pass
                elif Vendredi == "on" and VendrediSelectDeb and VendrediSelectFin and VendrediSelectDeb < VendrediSelectFin :
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=5,
                                                    heure_debut=listHoraire.get(pk=VendrediSelectDeb),
                                                    heure_fin=listHoraire.get(pk=VendrediSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Vendredi'] = 'Merci de sélectionner une heure de début & de fin cohérente'

                #--------------------------------------------------------------------------------------------
                if Samedi==None:
                    pass
                elif Samedi == "on" and SamediSelectDeb and SamediSelectFin and SamediSelectDeb < SamediSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=6,
                                                    heure_debut=listHoraire.get(pk=SamediSelectDeb),
                                                    heure_fin=listHoraire.get(pk=SamediSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Samedi'] = 'Merci de sélectionner une heure de début & de fin cohérente'

                if Dimanche==None:
                    pass
                elif Dimanche == "on" and DimancheSelectDeb and DimancheSelectFin and DimancheSelectDeb < DimancheSelectFin:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,
                                                    jours_semaine_id=7,
                                                    heure_debut=listHoraire.get(pk=DimancheSelectDeb),
                                                    heure_fin=listHoraire.get(pk=DimancheSelectFin)
                                                )
                    Jour.save()
                else:
                    errorsDateMarche['Dimanche'] = 'Merci de sélectionner une heure de début & de fin cohérente'
                
                context['marche']= marche
                context['JourMarcheJson']=jourMarche

                for j in jourMarche.values('jours_semaine','jours_semaine__jours','heure_debut','heure_fin'):
                    context['jour_{}'.format(j['jours_semaine'])]=j
                context['errorsDateMarche']=errorsDateMarche.items()
                result.append(list(Marches.objects.select_related().filter(pk=marche.id).values('adresse__latitude','adresse__longitude')))
                context['carte']=result
                return HttpResponseRedirect(reverse('market:fiche_marche', args=(marche.id,)))
                      
            



            context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche)   
            context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse) 
            result.append(list(Marches.objects.select_related().filter(pk=marche.id).values('adresse__latitude','adresse__longitude')))
            context['carte']=result
            context['errorsDateMarche']=errorsDateMarche.items()

        else:
            context['errorsMarche'] = formMarche.errors.items()
            context['errorsAdresse'] = formAdresse.errors.items()
            context['errorsDateMarche']=errorsDateMarche.items()


    context['marche']= marche
    context['JourMarcheJson']=jourMarche
    

    for e in Marches.objects.select_related().filter(pk=marche.id).values('nom','nb_exposant','adresse__adresse','adresse__cp','adresse__ville','adresse__latitude','adresse__longitude'):
        context['nom']=e['nom'] 
        context['nb_exposant']="vide" if e['nb_exposant']==None else e['nb_exposant']
        context['adresse__adresse']=e['adresse__adresse']
        context['adresse__cp']=e['adresse__cp']
        context['adresse__ville']=e['adresse__ville']
        context['adresse__latitude']="{:10.4f}".format(e['adresse__latitude'])
        context['adresse__longitude']="{:10.4f}".format(e['adresse__longitude'])

    context['date_marche']=""
    for e in Marches.objects.select_related().filter(pk=marche.id).values('jourmarche__jours_semaine__jours','jourmarche__heure_debut__label','jourmarche__heure_fin__label').order_by('jourmarche__jours_semaine'):
        context['date_marche']+="{} : {} - {} ---------".format(e['jourmarche__jours_semaine__jours'],e['jourmarche__heure_debut__label'],e['jourmarche__heure_fin__label'])


    for j in jourMarche.values('jours_semaine','jours_semaine__jours','heure_debut','heure_fin'):
        context['jour_{}'.format(j['jours_semaine'])]=j

    return render(request, 'market/fiche_marche.html', context)
