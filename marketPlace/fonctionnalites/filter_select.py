from marketPlace.models import Produits,RefCategorie,MiseEnVente
from django.http import JsonResponse
from django.db.models import Q



def categorieSelect(request):
    search_qsCategories = RefCategorie.objects.filter(label__istartswith=request.GET['searchCategorie'] ).values('id', 'label')
    return JsonResponse({'results': list(search_qsCategories)})

def produitSelect(request):
    produitsDejaEnVente = list(MiseEnVente.objects.values_list('produit_id', flat=True).filter(producteur_id=request.GET['idProducteur']))

    search_qsProduits = Produits.objects.filter(Q(nom__istartswith=request.GET['searchProduit']) &
                                                Q(categorie_id=request.GET['searchCategorie']) &
                                                ~Q(pk__in=produitsDejaEnVente)).values('id', 'nom')
    
    return JsonResponse({'results': list(search_qsProduits)})
