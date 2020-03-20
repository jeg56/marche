from produit.forms import ParagraphErrorList,ProduitsForm
from django.db import transaction
from django.shortcuts import render,get_object_or_404
from marketPlace.models import Producteurs,RefCategorie,Produits,MiseEnVente
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Max

@transaction.atomic
def add_produit(request,id,producteur=None):
    producteur=get_object_or_404(Producteurs,pk=id)
    produitsAVendre=MiseEnVente.objects.filter(producteur_id=producteur.id)
    context = {
        'title': 'Infos sur les produits',
        'id':id,
        'producteur':producteur,
        'produitsAVendre':produitsAVendre,
    }
  

    if request.path==('/producteur/{}/add_produit'.format(id)):
        context['fiche_produit']=True
  
        return render(request, 'producteur/fiche_producteur.html', context)
    else:
        return context

@transaction.atomic
def save_produit_producteur(request,id,producteur=None):


    producteur=get_object_or_404(Producteurs,pk=id)
    produitsAVendre=MiseEnVente.objects.filter(producteur_id=producteur.id)
    context = {
        'title': 'Liste des produits',
        'producteur':producteur,
    }
    if request.method == 'POST':
        orderProduit = request.POST.get('input-ordre-produit-producteur')
        for idx, val in enumerate(orderProduit.split(',')):
            MiseEnVente.objects.filter(producteur_id=producteur.id,produit=val).update(ordre_affichage=idx)
   

    produitsAVendre=MiseEnVente.objects.filter(producteur_id=producteur.id).order_by('ordre_affichage')
    context['produitsAVendre']=produitsAVendre

    if request.path==('/producteur/{}/save_produit_producteur'.format(id)):
        context['fiche_produit']=True

        return HttpResponseRedirect(reverse('producteur:fiche_produit', args=(id,)))

                     
    else:
        return context


@transaction.atomic
def fiche_produit(request,id,producteur=None):
    if producteur==None:  
        producteur=get_object_or_404(Producteurs,pk=id)
    
    produits=list(Produits.objects.values())

    refCategories=RefCategorie.objects.all()

    context = {
        'title': 'Liste des produits',
        'producteur':producteur,
    }

    identifie=True if  'id' in request.session and producteur.connexions_id==request.session['id'] else False
    readOnlyField=False if  'id' in request.session and producteur.connexions_id==request.session['id'] else True

    context['formProduit'] =ProduitsForm(data=request.POST,error_class=ParagraphErrorList)
    
    if request.method == 'POST':
        produit=Produits.objects.values()
        formProduit=ProduitsForm(data=request.POST,error_class=ParagraphErrorList)

        if formProduit.is_valid():
            produit= Produits.objects.get(nom=formProduit.cleaned_data['nom'])
            max_ordre_affichage=MiseEnVente.objects.filter(producteur_id=producteur.id).aggregate(Max('ordre_affichage')).get('ordre_affichage__max')
     
            addMiseEnVente , created = MiseEnVente.objects.get_or_create(
                produit=produit,
                producteur=producteur,
                prix=0,
                ordre_affichage=max_ordre_affichage+1,
                etat_stock=True)

            addMiseEnVente.save()

        else:
            context['errors'] = formProduit.errors.items()




    produitsAVendre=MiseEnVente.objects.filter(producteur_id=producteur.id).order_by('ordre_affichage')
    context['produitsAVendre']=produitsAVendre


    if request.path==('/producteur/{}/produits'.format(id)):
        context['fiche_produit']=True
        return render(request, 'producteur/fiche_producteur.html', context)
    else:
        return context