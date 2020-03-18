from marketPlace.models import Produits,RefCategorie,RefFamille
from django.http import JsonResponse
from django.db.models import Q



def familleSelect(request):
    search_qsFamilles = RefFamille.objects.filter(label__istartswith=request.GET['searchFamille'] ).values('id', 'label')
    return JsonResponse({'results': list(search_qsFamilles)})

def categorieSelect(request):
    search_qsCategories = RefCategorie.objects.filter(famille_id=request.GET['searchFamille'] ).values('id', 'label')
    return JsonResponse({'results': list(search_qsCategories)})

def produitSelect(request):
    search_qsProduits = Produits.objects.filter(nom__istartswith=request.GET['searchProduit'],categorie_id=request.GET['searchCategorie']).values('id', 'nom')
    return JsonResponse({'results': list(search_qsProduits)})
