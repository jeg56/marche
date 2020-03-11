# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from marketPlace.models import Marches,Adresses,RefManifestation,RefFrequence,RefHoraire,Communes
from marketPlace.forms import ParagraphErrorList,AdressesForm
from django.shortcuts import render,get_object_or_404
from .forms import MarchesForm
from django.db import transaction
from marketPlace.fonctionnalites import getLocalisation
from django.contrib.auth.decorators import login_required

#@login_required(login_url='connexion:identification')
@transaction.atomic
def fiche_marche(request,id=None):
    if request.path=='/market/add/':
        marche=Marches()
        adresse=Adresses.objects.create()
        marche.adresse=adresse
        marche.id=0
    else:
        marche=get_object_or_404(Marches,pk=id)
        adresse= marche.adresse

    context = {
        'title': 'Infos sur le marché',
        'marche': marche,
    }

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
        formAdresse=AdressesForm(readOnlyField=readOnlyField,adresse=adresse,data=request.POST, error_class=ParagraphErrorList)


        if formAdresse.is_valid() and formMarche.is_valid():
            adrs = formAdresse.cleaned_data['adresse']
            cp = formAdresse.cleaned_data['cp']
            ville = formAdresse.cleaned_data['ville']

            if(adresse.adresse!=adrs or adresse.cp!=cp or adresse.ville)!=ville:
                rechercheGeocodage=adrs+' '+cp +' '+ ville
                latitude,longitude=getLocalisation.getLocalisation(rechercheGeocodage)
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

            marche.nom=nom
            marche.manifestation=manifestation
            marche.frequence=frequence
            marche.heure_debut=heure_debut
            marche.heure_fin=heure_fin
            marche.nb_exposant=nb_exposant

 
            marche.historique=('{} maj par {} \n').format(marche.historique,request.session['identifiant']) if marche.historique else ('maj par {} \n').format(request.session['identifiant'])
            marche.save()

            context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche)   
            context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)    
        else:
            context['errorsMarche'] = formMarche.errors.items()
            context['errorsAdresse'] = formAdresse.errors.items()
    return render(request, 'market/fiche_marche.html', context)



@login_required(login_url='connexion:identification')
@transaction.atomic
def add_marche(request):
    
    marche=Marches()
    adresse=Adresses()


    context = {
        'title': 'Déclaration d''nouveau marché',
    }

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
        formAdresse=AdressesForm(readOnlyField=readOnlyField,adresse=adresse,data=request.POST, error_class=ParagraphErrorList)


        if formAdresse.is_valid() and formMarche.is_valid():
            adrs = formAdresse.cleaned_data['adresse']
            cp = formAdresse.cleaned_data['cp']
            ville = formAdresse.cleaned_data['ville']

            if(adresse.adresse!=adrs or adresse.cp!=cp or adresse.ville)!=ville:
                rechercheGeocodage=adrs+' '+cp +' '+ ville
                latitude,longitude=getLocalisation.getLocalisation(rechercheGeocodage)
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

            marche.nom=nom
            marche.manifestation=manifestation
            marche.frequence=frequence
            marche.heure_debut=heure_debut
            marche.heure_fin=heure_fin
            marche.nb_exposant=nb_exposant

 
            marche.historique=('{} maj par {} \n').format(marche.historique,request.session['identifiant']) if marche.historique else ('maj par {} \n').format(request.session['identifiant'])
            marche.save()

            context['formMarche']=MarchesForm(readOnlyField=readOnlyField,marche=marche)   
            context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)    



        else:
            context['errorsMarche'] = formMarche.errors.items()
            context['errorsAdresse'] = formAdresse.errors.items()


    

    return render(request, 'market/fiche_marche.html', context)


    
    