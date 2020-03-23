from market.forms import MarchesForm
from django.db import transaction
from django.shortcuts import render,get_object_or_404
from marketPlace.models import Producteurs,Marches
from django.urls import reverse
from django.http import HttpResponseRedirect

def fiche_marche(request,id,producteur=None):
    context = {
        'title': 'Liste des marchés',
    }
    
    if request.path==('/producteur/{}/marches'.format(id)):
        context['fiche_marche']=True

        return render(request, 'producteur/fiche_producteur.html', context)
    else:
        return context