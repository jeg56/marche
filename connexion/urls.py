from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^$', views.identification,name='identification'), 
    url(r'^inscription$', views.inscription_producteur,name='inscription_producteur'), 
    url(r'^inscription/(?P<id>[A-Za-z0-9]+)/$', views.inscription_valider,name='inscription_valider'), 
]

