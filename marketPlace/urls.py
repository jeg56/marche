"""marketPlace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


from marketPlace import views as marketPlace_views
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static

from marketPlace.fonctionnalites import autocomplete 


urlpatterns = [

    url(r'^ville-autocomplete/$',autocomplete.VilleAutocomplete, name='ville-autocomplete',),
    url(r'^cp-autocomplete/$',autocomplete.CPAutocomplete, name='cp-autocomplete',),

    url(r'^connexion/', include(('connexion.urls', 'connexion'), namespace='connexion')),
    url(r'^producteur/', include(('producteur.urls', 'producteur'), namespace='producteur')),
    url(r'^market/', include(('market.urls', 'market'), namespace='market')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = marketPlace_views.handler404
handler500 = marketPlace_views.handler500

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns