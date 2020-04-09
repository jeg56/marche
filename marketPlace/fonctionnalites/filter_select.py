from marketPlace.models import Produits,RefCategorie,MiseEnVente,Adresses,Marches
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Avg,Min,Max,F



def departementSelect(request):
    #search_qsCentroid= Adresses.objects.raw("select avg(longitude) as longitude  from adresses where cp like '"+ request.GET['searchCP']  +"%' group by substr(cp,1,2)")
    if request.GET['searchCP']=="-1":
        search_qsAdresse = Marches.objects.select_related().filter(Q(jourmarche__jours_semaine__isnull=False)            
                                                         ).values('id','nom','nb_exposant','adresse__latitude', 'adresse__longitude','adresse__adresse','adresse__cp','adresse__ville','jourmarche__jours_semaine','jourmarche__heure_debut__label','jourmarche__heure_fin__label')
      
    else: 
        search_qsAdresse = Marches.objects.select_related().filter(Q(adresse__cp__istartswith=request.GET['searchCP'])  &
                                                                Q(jourmarche__jours_semaine__isnull=False)            
                                                         ).values('id','nom','nb_exposant','adresse__latitude', 'adresse__longitude','adresse__adresse','adresse__cp','adresse__ville','jourmarche__jours_semaine','jourmarche__heure_debut__label','jourmarche__heure_fin__label')
    
    #search_qsAdresse = Marches.objects.select_related().filter(adresse__cp__istartswith='35').values('nom','adresse__latitude', 'adresse__longitude','adresse__adresse','adresse__cp','adresse__ville')
    resultMoy=search_qsAdresse.values('jourmarche__jours_semaine__jours').annotate(
                    latitude__avg=Avg('adresse__latitude'),
                    longitude__avg=Avg('adresse__longitude'),
                    latitude__min=Min('adresse__latitude'),
                    longitude__min=Min('adresse__longitude'),
                    latitude__max=Max('adresse__latitude'),
                    longitude__max=Max('adresse__longitude')
                ).order_by('jourmarche__jours_semaine')

    result = []

    result.append(list(resultMoy))
    result.append(list(search_qsAdresse))

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
