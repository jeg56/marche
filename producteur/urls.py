
from django.conf.urls import url
from django.conf import settings
from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', views.fiche_producteur,name='fiche_producteur'), 
]
