from marketPlace.fonctionnalites import filter_select
from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^produit-filter/$', filter_select.produitSelect,name='produit-filter'),
    url(r'^categorie-filter/$', filter_select.categorieSelect,name='categorie-filter'), 
]


