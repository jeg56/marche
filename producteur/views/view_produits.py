from produit.forms import ParagraphErrorList,ProduitsForm
from django.db import transaction
from django.shortcuts import render,get_object_or_404
from marketPlace.models import Producteurs,RefCategorie,RefFamille,Produits,MiseEnVente

@transaction.atomic
def fiche_produit(request,id,producteur=None):
    if producteur==None:  
        producteur=get_object_or_404(Producteurs,pk=id)
    
    produits=list(Produits.objects.values())

    refFamilles=RefFamille.objects.all()
    refCategories=RefCategorie.objects.all()

    produitsAVendre=MiseEnVente.objects.filter(producteur_id=producteur.id)


    context = {
        'title': 'Liste des produits',
        'producteur':producteur,
        'produitsAVendre':produitsAVendre
    }


    identifie=True if  'id' in request.session and producteur.connexions_id==request.session['id'] else False
    readOnlyField=False if  'id' in request.session and producteur.connexions_id==request.session['id'] else True

    context['formProduit']=ProduitsForm(readOnlyField=readOnlyField,refCategorie=refCategories,refFamille=refFamilles,produit=produits)











    if request.path==('/producteur/{}/produits'.format(id)):
        context['fiche_produit']=True
        return render(request, 'producteur/fiche_producteur.html', context)
    else:
        return context