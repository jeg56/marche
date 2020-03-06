# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import FicheProducteurForm,ParagraphErrorList
from marketPlace.models import Producteurs,RefMetier
from django.http import Http404
from django.shortcuts import render,get_object_or_404

# Create your views here.
def fiche_producteur(request,id):
    
    producteur=get_object_or_404(Producteurs,pk=id)

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
        context['form']=FicheProducteurForm(readOnlyField=readOnlyField,idProducteur=producteur.id)
        
    else:
        context['form']=FicheProducteurForm(readOnlyField=readOnlyField,idProducteur=producteur.id)
       


    if request.method == 'POST':
        form = FicheProducteurForm(readOnlyField=readOnlyField,idProducteur=producteur.id, data=request.POST or request.FILES, error_class=ParagraphErrorList)
        if form.is_valid():
           
            nom = form.cleaned_data['nom']

            metier = form.cleaned_data['metier']
            raison_social = form.cleaned_data['raison_social']
            num_siren = form.cleaned_data['num_siren']
            description= form.cleaned_data['description']
            num_telephone_fix= form.cleaned_data['num_telephone_fix']
            num_telephone_portable= form.cleaned_data['num_telephone_portable']
            metier=RefMetier.objects.get(pk=metier)

            producteur.nom=nom
            producteur.photo = request.FILES['photo']
            producteur.metier=metier
            producteur.raison_social=raison_social
            producteur.num_siren=num_siren
            producteur.description=description
            producteur.num_telephone_fix=num_telephone_fix
            producteur.num_telephone_portable=num_telephone_portable

            producteur.save()
            
     
            context['producteur']: producteur
            context['form']=FicheProducteurForm(readOnlyField=readOnlyField,idProducteur=producteur.id)


    context['identifie']=identifie
    return render(request, 'producteur/fiche_producteur.html', context)

