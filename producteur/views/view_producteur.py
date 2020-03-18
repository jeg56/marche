# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from producteur.forms import ProducteurForm
from marketPlace.forms import ParagraphErrorList,AdressesForm
from marketPlace.models import Producteurs,RefMetier,Adresses
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from marketPlace.fonctionnalites import getLocalisation
from codecs import encode 

#@login_required(login_url='connexion:identification')
@transaction.atomic
def fiche_producteur(request,id,producteur=None):   
    if producteur==None:  
        producteur=get_object_or_404(Producteurs,pk=id)
        
    adresse= producteur.adresse
    refMetier=RefMetier.objects.all()
    context = {
        'title': 'Infos sur le producteur',
        'producteur': producteur,
    }
    #if not producteur:
    #   raise Http404()

    # on regarde si le producteur est identifié ( loggué )
    identifie=False
    readOnlyField=True

    if 'id' in request.session and producteur.connexions_id==request.session['id']:
        readOnlyField=False
        identifie=True
        context['formProducteur']=ProducteurForm(readOnlyField=readOnlyField,producteur=producteur,refMetier=refMetier)
        context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)    
    else:
        context['formProducteur']=ProducteurForm(readOnlyField=readOnlyField,producteur=producteur,refMetier=refMetier)
        context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)

    if request.method == 'POST':
        formAdresse=AdressesForm(readOnlyField=readOnlyField,adresse=adresse,data=request.POST, error_class=ParagraphErrorList)
        formProducteur = ProducteurForm(readOnlyField=readOnlyField,producteur=producteur,refMetier=refMetier, data=request.POST or request.FILES, error_class=ParagraphErrorList)
        if formAdresse.is_valid() and formProducteur.is_valid():
            adrs = formAdresse.cleaned_data['adresse']
            cp = formAdresse.cleaned_data['cp']
            ville = formAdresse.cleaned_data['ville']

            if(adresse.adresse!=adrs or adresse.cp!=cp or adresse.ville!=ville):
                rechercheGeocodage=adrs+' '+cp +' '+ ville
                latitude,longitude=getLocalisation.getLocalisation(rechercheGeocodage)
                adresse , created = Adresses.objects.get_or_create(adresse=adrs,cp=cp,ville=ville)
                adresse.latitude=latitude
                adresse.longitude=longitude
                adresse.save()
                producteur.adresse=adresse

            nom = formProducteur.cleaned_data['nom']
            if request.FILES.get('photo'):    
                photo=request.FILES['photo']
                producteur.photo = photo

            metier = formProducteur.cleaned_data['metier']
            raison_social = formProducteur.cleaned_data['raison_social']
            num_siren = formProducteur.cleaned_data['num_siren']
            description= formProducteur.cleaned_data['description']
            num_telephone_fix= formProducteur.cleaned_data['num_telephone_fix']
            num_telephone_portable= formProducteur.cleaned_data['num_telephone_portable']
            metier=refMetier.objects.get(pk=metier)

            producteur.nom=nom
            producteur.metier=metier
            producteur.raison_social=raison_social
            producteur.num_siren=num_siren
            producteur.description=description
            producteur.num_telephone_fix=num_telephone_fix
            producteur.num_telephone_portable=num_telephone_portable
            producteur.save()
            
     
            context['producteur']: producteur
            context['adresse']: adresse

            context['formProducteur']=ProducteurForm(readOnlyField=readOnlyField,producteur=producteur,refMetier=refMetier)
            context['formAdresse']=AdressesForm(readOnlyField=readOnlyField,adresse=adresse)    
            


    context['identifie']=identifie

    if request.path==('/producteur/{}/producteur'.format(id)): 
        context['fiche_producteur']=True
        return render(request, 'producteur/fiche_producteur.html', context)
    else:
        return context


