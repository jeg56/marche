# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import FicheProducteurForm,ParagraphErrorList
from marketPlace.models import Producteurs
from django.http import Http404

from django.shortcuts import render

# Create your views here.
def fiche_producteur(request,id):
    producteur=Producteurs.objects.get(pk=id)

    context = {
        'title': 'Infos sur le producteur',
        'producteur': producteur,
    }
    if not producteur:
        raise Http404()


    if 'id' in request.session and producteur.connexions_id==request.session['id']:
        context['form']=FicheProducteurForm(readOnlyField=False,auto_id=False)
    else:
        context['form']=FicheProducteurForm(readOnlyField=True,auto_id=False)
    f = FicheProducteurForm(readOnlyField=False,auto_id=False)

    context['test']=f

    return render(request, 'producteur/fiche_producteur.html', context)


