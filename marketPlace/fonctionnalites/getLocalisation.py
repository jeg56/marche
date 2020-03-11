# -*- coding: utf-8 -*-

import urllib.request, json
import logging

logger = logging.getLogger(__name__)
def getLocalisation(adresse):
    latitude="0"
    longitude="0"
    data=""

    urlAdrs="https://nominatim.openstreetmap.org/search?format=json&q={}" .format(urllib.parse.quote(adresse))
    url = urllib.parse.quote(urlAdrs)
    with urllib.request.urlopen(urlAdrs) as url:
        try:
            data=json.loads(url.read())[0]
            latitude=data['lat']
            longitude=data['lon']
            
        except Exception as e:
            logger.error('GetLocalisation : {} - {} - retour url : {} '.format(adresse,e,data))

    print(latitude +' '+ longitude)
    return latitude,longitude





