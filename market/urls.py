from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.fiche_marche,name='fiche_marche'), 
    url(r'^add/$', views.fiche_marche), 
]
