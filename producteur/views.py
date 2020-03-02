# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import FicheProducteurForm,ParagraphErrorList
from marketPlace.models import Producteurs

from django.shortcuts import render

# Create your views here.
def fiche_producteur(request,id):
    producteur=Producteurs.objects.get(pk=id)
    print(id)
    context = {
        'title': 'Infos sur le producteur',
        'producteur': producteur,
    }

    context['form']=FicheProducteurForm()
    return render(request, 'producteur/fiche_producteur.html', context)


