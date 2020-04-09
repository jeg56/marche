
function pushpinClicked_1(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infobox['1'].setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true,

          actions: [{
            label: "Plus d'infos",
            eventHandler: function () {
              window.location.href = "/market/"+e.target.metadata.zIndex
            }
          }]


      });

      $('.carousel').carousel('pause');
  }
}
function pushpinClicked_2(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infobox['2'].setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true,
          actions: [{
            label: "Plus d'infos",
            eventHandler: function () {
              window.location.href = "/market/"+e.target.metadata.zIndex
            }
          }]
      });

      $('.carousel').carousel('pause');
  }
}
function pushpinClicked_3(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infobox['3'].setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true,
          actions: [{
            label: "Plus d'infos",
            eventHandler: function () {
              window.location.href = "/market/"+e.target.metadata.zIndex
            }
          }]
      });

      $('.carousel').carousel('pause');
  }
}
function pushpinClicked_4(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infobox['4'].setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true,
          actions: [{
            label: "Plus d'infos",
            eventHandler: function () {
              window.location.href = "/market/"+e.target.metadata.zIndex
            }
          }]
      });

      $('.carousel').carousel('pause');
  }
}
function pushpinClicked_5(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infobox['5'].setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true,
          actions: [{
            label: "Plus d'infos",
            eventHandler: function () {
              window.location.href = "/market/"+e.target.metadata.zIndex
            }
          }]
      });

      $('.carousel').carousel('pause');
  }
}
function pushpinClicked_6(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infobox['6'].setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true,
          actions: [{
            label: "Plus d'infos",
            eventHandler: function () {
              window.location.href = "/market/"+e.target.metadata.zIndex
            }
          }]
      });

      $('.carousel').carousel('pause');
  }
}
function pushpinClicked_7(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infobox['7'].setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true,
          actions: [{
            label: "Plus d'infos",
            eventHandler: function () {
              window.location.href = "/market/"+e.target.metadata.zIndex
            }
          }]
      });

      $('.carousel').carousel('pause');
  }
}
function centerCarte(element,joursLettre,joursInt){
    var lat = element.latitude__avg
    var lon = element.longitude__avg
    var lat_min = element.latitude__min
    var lon_min = element.longitude__min
    var lat_max = element.latitude__max
    var lon_max = element.longitude__max
  
    box=new Microsoft.Maps.LocationRect.fromEdges(lat_max,lon_min,lat_min,lon_max);

    map[joursInt]= new Microsoft.Maps.Map('#'+joursLettre, {
      center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon)),
      bounds: box
    });
  
    //Create an infobox at the center of the map but don't show it.
    infobox[joursInt] = new Microsoft.Maps.Infobox(map[joursInt].getCenter(), {
        visible: false
    });
        //Assign the infobox to a map instance.
  infobox[joursInt].setMap(map[joursInt]);
}

function GetMap() {
  map=[]
  infobox=[]
  dataCoordAdresse.results[0].forEach(element => {
    
    switch(element.jourmarche__jours_semaine__jours) {
      case 'Lundi':
        centerCarte(element,'Lundi','1')
        break;
      case 'Mardi':
        centerCarte(element,'Mardi','2')
        break;
      case 'Mercredi':
        centerCarte(element,'Mercredi','3')
        break;
      case 'Jeudi':
        centerCarte(element,'Jeudi','4')
        break;
      case 'Vendredi':
        centerCarte(element,'Vendredi','5')
        break;
      case 'Samedi':
        centerCarte(element,'Samedi','6')
        break;
      case 'Dimanche':
        centerCarte(element,'Dimanche','7')
        break;
    } 
  })



   dataCoordAdresse.results[1].forEach(element => {
    var lat = element.adresse__latitude
    var lon = element.adresse__longitude
    locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
    var pin  = new Microsoft.Maps.Pushpin(locs);
    nbExpo=element.nb_exposant==null?"":"Nbre d'exposant :" +element.nb_exposant +"<br>"
    pin.metadata = {
      title: element.nom,
      zIndex:element.id,
      description: nbExpo+ element.adresse__adresse +' '+ element.adresse__cp +' ' + element.adresse__ville + '<br> Ouverture : ' + element.jourmarche__heure_debut__label + ' - ' + element.jourmarche__heure_fin__label
    };

     //Add a click event handler to the pushpin.

     switch(element.jourmarche__jours_semaine) {
       
      case 1:
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked_1);
        break;
      case 2:
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked_2);
        break;
      case 3:
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked_3);
        break;
      case 4:
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked_4);
        break;
      case 5:
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked_5);
        break;
      case 6:
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked_6);
        break;
      case 7:
        Microsoft.Maps.Events.addHandler(pin, 'click', pushpinClicked_7);
        break;

    }


     //Add pushpin to the map.
     map[element.jourmarche__jours_semaine].entities.push(pin);

  }) 
  //-----------------------------------------------------------------------------------------
}
