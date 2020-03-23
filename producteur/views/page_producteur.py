from . import view_producteur 
from . import view_produits 
from . import view_marches 
from django.shortcuts import render,get_object_or_404
from django.views import View
from marketPlace.models import Producteurs,RefMetier,Adresses
from copy import deepcopy

def page_producteur(request,id):
        producteur=get_object_or_404(Producteurs,pk=id)
        context_producteur=view_producteur.fiche_producteur(request,id,producteur)
        context_produit=view_produits.fiche_produit(request,id,producteur)
        context_marche=view_marches.fiche_marche(request,id,producteur)

        context = {** context_producteur,**context_produit,**context_marche}
        context['fiche_produit']=True
        context['fiche_producteur']=True
        context['fiche_marche']=True
        return render(request, 'producteur/fiche_producteur.html', context)


