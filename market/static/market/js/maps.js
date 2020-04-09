
function pushpinClicked(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.



  }
}

function GetMapCarte() {

    coef_plus=1.1
    coef_moins=0.9
    box=new Microsoft.Maps.LocationRect.fromEdges(coef_plus*dataCoordAdresse.adresse__latitude,coef_moins*dataCoordAdresse.adresse__longitude,coef_moins*dataCoordAdresse.adresse__latitude,coef_plus*dataCoordAdresse.adresse__longitude);
    

    map= new Microsoft.Maps.Map('#zone_carte', {
      center: new Microsoft.Maps.Location(parseFloat(dataCoordAdresse.adresse__latitude), parseFloat(dataCoordAdresse.adresse__longitude)),
      bounds: box
    });

    //Create an infobox at the center of the map but don't show it.
    infobox = new Microsoft.Maps.Infobox(map.getCenter(), {
        visible: false
    });

    var lat = dataCoordAdresse.adresse__latitude
    var lon = dataCoordAdresse.adresse__longitude
    locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
    locsInfos= new Microsoft.Maps.Location(parseFloat(lat+1), parseFloat(lon));

        //Assign the infobox to a map instance.
        infobox.setMap(map);
        nbExpo=dataCoordAdresse.nb_exposant=="vide"?"":"Nbre d'exposant :" +dataCoordAdresse.nb_exposant +"<br>"
        infobox.setOptions({
          location: locsInfos,
          title: dataCoordAdresse.nom,
          description: nbExpo+ dataCoordAdresse.adresse__adresse +' '+ dataCoordAdresse.adresse__cp +' ' + dataCoordAdresse.adresse__ville +"<br>" + dataCoordAdresse.date_marche,
          visible: true
      });

      var pin  = new Microsoft.Maps.Pushpin(locs);
     //Add pushpin to the map.
     map.entities.push(pin);
     console.error(dataCoordAdresse.adresse__latitude)
  //-----------------------------------------------------------------------------------------
}
var elements = document.getElementsByClassName("Infobox");

var myFunction = function() {

    alert('jhhhhhhhhhhhhhhhhhhhhh');
};

for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', myFunction, false);
}