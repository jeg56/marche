# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ConnexionProducteurForm
from marketPlace.models import Connexions

def identification(request):
    context = {
        'title': 'Mon super titre',
        'message': None,
        }



    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            nom = form.cleaned_data['name']

            contact = Contact.objects.filter(email=email)
            if not contact.exists():
                # If a contact is not registered, create a new one.
                contact = Contact.objects.create(
                    email=email,
                    nom=nom
                )
            album.save()


        context['message']= 'Inscription en cours - Email envoyé'
        
    return render(request, 'connexion/identification.html', context)
    




def inscription_producteur(request):
    print(" -------------------- On entre dans la vue inscription producteur")
    context = {
        'title': 'Formulaire d\'inscription des producteurs',
        'message': None,
        }
    if request.method == 'POST':
        print(" -------------------- dans la methode POST")
        form = ConnexionProducteurForm(request.POST)
        if form.is_valid():
            print(" -********************************************************************** valid")
            identifiant = form.cleaned_data['identifiant']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            opt_in = form.cleaned_data['opt_in']
            

            connexion = Connexions.objects.filter(email=email)
            if not connexion.exists():
                # If a contact is not registered, create a new one.
                connexion = Connexions.objects.create(
                    identifiant=identifiant,
                    password=password,
                    email=email,
                    opt_in=opt_in,
                    etat_connexion=False
                )
                connexion.save()
                print(" -------------------- Enregistrement effectué")
        else:
            print(" -------------------- Error")
            for key, error in form.errors.items():
                print('{} - {} '.format(key,error))




            context['errors'] = form.errors.items()

        context['message']= 'Inscription en cours - Email envoyé'
        
    return render(request, 'connexion/inscription_producteur.html', context)
    