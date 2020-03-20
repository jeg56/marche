
from django.conf.urls import url
from django.conf import settings
from producteur.views import page_producteur,view_producteur,view_produits


urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', page_producteur.page_producteur,name='producteur'), 
    url(r'^(?P<id>[0-9]+)/producteur$', view_producteur.fiche_producteur,name='fiche_producteur'), 
    url(r'^(?P<id>[0-9]+)/produits$', view_produits.fiche_produit,name='fiche_produit'), 
    url(r'^(?P<id>[0-9]+)/add_produit$', view_produits.add_produit,name='add_produit'), 
    url(r'^(?P<id>[0-9]+)/save_produit_producteur', view_produits.save_produit_producteur,name='save_produit_producteur'), 
]