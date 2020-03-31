from marketPlace.models import Produits,RefCategorie,MiseEnVente,Adresses,Marches
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Avg,Min,Max



def departementSelect(request):
    #search_qsCentroid= Adresses.objects.raw("select avg(longitude) as longitude  from adresses where cp like '"+ request.GET['searchCP']  +"%' group by substr(cp,1,2)")

    search_qsAdresse = Marches.objects.select_related().filter(adresse__cp__istartswith=request.GET['searchCP']).values('nom','nb_exposant','adresse__latitude', 'adresse__longitude','adresse__adresse','adresse__cp','adresse__ville')
    
    #search_qsAdresse = Marches.objects.select_related().filter(adresse__cp__istartswith='35').values('nom','adresse__latitude', 'adresse__longitude','adresse__adresse','adresse__cp','adresse__ville')
    
    result = [{
            'latitude__avg':search_qsAdresse.aggregate(Avg('adresse__latitude'))['adresse__latitude__avg'],
            'longitude__avg':search_qsAdresse.aggregate(Avg('adresse__longitude'))['adresse__longitude__avg'],
            'latitude__min':search_qsAdresse.aggregate(Min('adresse__latitude'))['adresse__latitude__min'],
            'longitude__min':search_qsAdresse.aggregate(Min('adresse__longitude'))['adresse__longitude__min'],
            'latitude__max':search_qsAdresse.aggregate(Max('adresse__latitude'))['adresse__latitude__max'],
            'longitude__max':search_qsAdresse.aggregate(Max('adresse__longitude'))['adresse__longitude__max']
            }]

    result.append(list(search_qsAdresse))
    print('--------------------------------------------------------------')
    print(result)
    print("--------------------------------------------------------------")
    return JsonResponse({'results': result })




def categorieSelect(request):
    search_qsCategories = RefCategorie.objects.filter(label__istartswith=request.GET['searchCategorie'] ).values('id', 'label')
    return JsonResponse({'results': list(search_qsCategories)})

def produitSelect(request):
    produitsDejaEnVente = list(MiseEnVente.objects.values_list('produit_id', flat=True).filter(producteur_id=request.GET['idProducteur']))

    search_qsProduits = Produits.objects.filter(Q(nom__istartswith=request.GET['searchProduit']) &
                                                Q(categorie_id=request.GET['searchCategorie']) &
                                                ~Q(pk__in=produitsDejaEnVente)).values('id', 'nom')
    
    return JsonResponse({'results': list(search_qsProduits)})
