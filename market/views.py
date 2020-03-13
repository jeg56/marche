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

#@login_required(login_url='connexion:identification')
@transaction.atomic
def fiche_marche(request,id=None):

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
      


    context = {
        'title': 'Infos sur le marché',
    }

    # on regarde si le producteur est identifié ( loggué )
    identifie=False
    readOnlyField=True

    
    if 'id' in request.session:
        readOnlyField=False
        identifie=True
        context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche,jourMarche=jourMarche)  
        context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)  
    else:
        context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche,jourMarche=jourMarche)   
        context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)    
    
    if request.method == 'POST':
        formMarche=MarchesForm(readOnlyField=readOnlyField,marche=marche,jourMarche=jourMarche,data=request.POST, error_class=ParagraphErrorList)
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
            frequence = formMarche.cleaned_data['frequence']
            heure_debut = formMarche.cleaned_data['heure_debut']
            heure_fin = formMarche.cleaned_data['heure_fin']
            nb_exposant= formMarche.cleaned_data['nb_exposant']

            manifestation=RefManifestation.objects.get(pk=manifestation)
            frequence=RefFrequence.objects.get(pk=frequence)
            heure_debut=RefHoraire.objects.get(pk=heure_debut)
            heure_fin=RefHoraire.objects.get(pk=heure_fin)
            
            jourMarche.delete()
            listJourMarche= formMarche.cleaned_data['JourSemaine']


            if id!='0':
                marche.nom=nom
                marche.manifestation=manifestation
                marche.frequence=frequence
                marche.heure_debut=heure_debut
                marche.heure_fin=heure_fin
                marche.nb_exposant=nb_exposant
                marche.historique=('{} maj par {} \n').format(marche.historique,request.session['identifiant']) if marche.historique else ('maj par {} \n').format(request.session['identifiant'])
                marche.save()
                for e in listJourMarche:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,jours_semaine_id=e)
                    Jour.save()
               

            else:                
                marche , created = Marches.objects.get_or_create(nom=nom,
                                                manifestation=manifestation,
                                                frequence=frequence,
                                                heure_debut=heure_debut,
                                                heure_fin=heure_fin,
                                                nb_exposant=nb_exposant,
                                                adresse=adresse,
                                                date_debut_id=1
                                                )
                marche.save()

                for e in listJourMarche:
                    Jour  = JourMarche.objects.create(ref_marche_id=marche.id,jours_semaine_id=e)
                    Jour.save()
                
                context['marche']= marche
                return HttpResponseRedirect(reverse('market:fiche_marche', args=(marche.id,)))
                      
            



            context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche,jourMarche=jourMarche)   
            context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)    
        else:
            context['errorsMarche'] = formMarche.errors.items()
            context['errorsAdresse'] = formAdresse.errors.items()

    context['marche']= marche
  
    return render(request, 'market/fiche_marche.html', context)
