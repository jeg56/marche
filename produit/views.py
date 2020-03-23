from django.shortcuts import render
from marketPlace.models import Produits,Producteurs,MiseEnVente
from django.db import transaction
from .forms import ParagraphErrorList,ProduitsForm
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import JsonResponse

def deleteMiseEnVente(request,idProducteur,id):
    context = {
        'title': 'Infos sur les produits',
    }
    miseEnVente=MiseEnVente.objects.filter(producteur_id=idProducteur,produit_id=id).delete()

    return  JsonResponse({'results': id})
