from marketPlace.models import Communes,Marches,Adresses
from django.http import JsonResponse
from django.db.models import Q





def VilleAutocomplete(request):
    search_qsVille = Communes.objects.filter(Q(ville__istartswith=request.GET['searchVille']) & Q(cp__istartswith=request.GET['searchCP'])).distinct('ville')[:5]
    results = []
    for r in search_qsVille:
        print(r.ville)
        results.append("{}" .format(r.ville))
    return JsonResponse(results, safe=False) 

def CPAutocomplete(request):
    search_qsCP = Communes.objects.filter(Q(ville__istartswith=request.GET['searchVille']) & Q(cp__istartswith=request.GET['searchCP']) ).distinct('cp')[:15]
    results = []
    for r in search_qsCP:
        results.append("{}" .format(r.cp))
    return JsonResponse(results, safe=False) 
