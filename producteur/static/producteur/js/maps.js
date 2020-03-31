
function pushpinClickedLundi(e) {
  //Make sure the infobox has metadata to display.
  if (e.target.metadata) {
      //Set the infobox options with the metadata of the pushpin.

      infoboxLundi.setOptions({
          location: e.target.getLocation(),
          title: e.target.metadata.title,
          description: e.target.metadata.description,
          visible: true
      });

      $('.carousel').carousel('pause');
  }
  }

function GetMap_Lundi() {

  var lat = dataCoordAdresse.results[0].latitude__avg
  var lon = dataCoordAdresse.results[0].longitude__avg
  var lat_min = dataCoordAdresse.results[0].latitude__min
  var lon_min = dataCoordAdresse.results[0].longitude__min
  var lat_max = dataCoordAdresse.results[0].latitude__max
  var lon_max = dataCoordAdresse.results[0].longitude__max

  box=new Microsoft.Maps.LocationRect.fromEdges(lat_max,lon_min,lat_min,lon_max);

  mapLundi = new Microsoft.Maps.Map('#lundi', {
    center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon)),
    bounds: box
  });

  //Create an infobox at the center of the map but don't show it.
  infoboxLundi = new Microsoft.Maps.Infobox(mapLundi.getCenter(), {
      visible: false
  });

    //Assign the infobox to a map instance.
    infoboxLundi.setMap(mapLundi);



   //-----------------------------------------------------------------------------------------


   dataCoordAdresse.results[1].forEach(element => {

    var lat = element.adresse__latitude
    var lon = element.adresse__longitude
    locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
    var pinLundi  = new Microsoft.Maps.Pushpin(locs);
    nbExpo=element.nb_exposant==null?"":"Nbre d'exposant :" +element.nb_exposant +"<br>"
    pinLundi.metadata = {
      title: element.nom,
      description: nbExpo+ element.adresse__adresse +' '+ element.adresse__cp +' ' + element.adresse__ville
    };

 
           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinLundi, 'click', pushpinClickedLundi);

           //Add pushpin to the map.
           mapLundi.entities.push(pinLundi);

  }) 
   






}




















// -------------------------------------------------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------------------------------------------------

   function GetMap() {
      var val = '47,43703290000'
      var lat = val.replace(",", ".");
      var val = '-2,08928090000'
      var lon = val.replace(",", ".");

       mapLundi = new Microsoft.Maps.Map('#lundi', {
         center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon))
       });
  
       //Create an infobox at the center of the map but don't show it.
       infoboxLundi = new Microsoft.Maps.Infobox(mapLundi.getCenter(), {
           visible: false
       });

       //Assign the infobox to a map instance.
       infoboxLundi.setMap(mapLundi);


       //-----------------------------------------------------------------------------------------
       
       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinLundi  = new Microsoft.Maps.Pushpin(locs);
 
     pinLundi.metadata = {
            title: 'Arnaud Jégoux',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinLundi, 'click', pushpinClickedLundi);

           //Add pushpin to the map.
           mapLundi.entities.push(pinLundi);


      //-----------------------------------------------------------------------------------------

       var val = '47,43803290000'
       var lat = val.replace(",", ".");
       var val = '-2,18928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinLundi  = new Microsoft.Maps.Pushpin(locs);
 
     pinLundi.metadata = {
            title: 'Marché de Ossé',
            description: 'place de la mairie 35410  Ossé'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinLundi, 'click', pushpinClickedLundi);

           //Add pushpin to the map.
           mapLundi.entities.push(pinLundi);


      //-----------------------------------------------------------------------------------------     
      
       var val = '47,48703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinLundi  = new Microsoft.Maps.Pushpin(locs);
 
     pinLundi.metadata = {
            title: 'marché de pontchat',
            description: '21 rue de Nantes 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinLundi, 'click', pushpinClickedLundi);

           //Add pushpin to the map.
           mapLundi.entities.push(pinLundi);
      
      //-----------------------------------------------------------------------------------------

       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,00928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinLundi  = new Microsoft.Maps.Pushpin(locs);
 
     pinLundi.metadata = {
            title: 'autre',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinLundi, 'click', pushpinClickedLundi);

           //Add pushpin to the map.
           mapLundi.entities.push(pinLundi);
      


  // ---------------------------------------------------------------------------------------------------------------------------
  // ---------------------------------------------------------------------------------------------------------------------------
  // --------------------------------------------------------------------------------------------------------------------------- 


      var val = '47,43703290000'
      var lat = val.replace(",", ".");
      var val = '-2,08928090000'
      var lon = val.replace(",", ".");

       mapMardi = new Microsoft.Maps.Map('#mardi', {
         center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon))
       });
  
       //Create an infobox at the center of the map but don't show it.
       infoboxMardi = new Microsoft.Maps.Infobox(mapMardi.getCenter(), {
           visible: false
       });

       //Assign the infobox to a map instance.
       infoboxMardi.setMap(mapMardi);


       //-----------------------------------------------------------------------------------------
       
       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMardi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMardi.metadata = {
            title: 'Arnaud Jégoux',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMardi, 'click', pushpinClickedMardi);

           //Add pushpin to the map.
           mapMardi.entities.push(pinMardi);


      //-----------------------------------------------------------------------------------------

       var val = '47,43803290000'
       var lat = val.replace(",", ".");
       var val = '-2,18928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMardi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMardi.metadata = {
            title: 'Marché de Ossé',
            description: 'place de la mairie 35410  Ossé'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMardi, 'click', pushpinClickedMardi);

           //Add pushpin to the map.
           mapMardi.entities.push(pinMardi);


      //-----------------------------------------------------------------------------------------     
      
       var val = '47,48703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMardi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMardi.metadata = {
            title: 'marché de pontchat',
            description: '21 rue de Nantes 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMardi, 'click', pushpinClickedMardi);

           //Add pushpin to the map.
           mapMardi.entities.push(pinMardi);
      
      //-----------------------------------------------------------------------------------------

       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,00928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMardi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMardi.metadata = {
            title: 'autre',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMardi, 'click', pushpinClickedMardi);

           //Add pushpin to the map.
           mapMardi.entities.push(pinMardi);
      


  // ---------------------------------------------------------------------------------------------------------------------------
  // ---------------------------------------------------------------------------------------------------------------------------
  // --------------------------------------------------------------------------------------------------------------------------- 


      var val = '47,43703290000'
      var lat = val.replace(",", ".");
      var val = '-2,08928090000'
      var lon = val.replace(",", ".");

       mapMercredi = new Microsoft.Maps.Map('#mercredi', {
         center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon))
       });
  
       //Create an infobox at the center of the map but don't show it.
       infoboxMercredi = new Microsoft.Maps.Infobox(mapMercredi.getCenter(), {
           visible: false
       });

       //Assign the infobox to a map instance.
       infoboxMercredi.setMap(mapMercredi);


       //-----------------------------------------------------------------------------------------
       
       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMercredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMercredi.metadata = {
            title: 'Arnaud Jégoux',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMercredi, 'click', pushpinClickedMercredi);

           //Add pushpin to the map.
           mapMercredi.entities.push(pinMercredi);


      //-----------------------------------------------------------------------------------------

       var val = '47,43803290000'
       var lat = val.replace(",", ".");
       var val = '-2,18928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMercredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMercredi.metadata = {
            title: 'Marché de Ossé',
            description: 'place de la mairie 35410  Ossé'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMercredi, 'click', pushpinClickedMercredi);

           //Add pushpin to the map.
           mapMercredi.entities.push(pinMercredi);


      //-----------------------------------------------------------------------------------------     
      
       var val = '47,48703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMercredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMercredi.metadata = {
            title: 'marché de pontchat',
            description: '21 rue de Nantes 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMercredi, 'click', pushpinClickedMercredi);

           //Add pushpin to the map.
           mapMercredi.entities.push(pinMercredi);
      
      //-----------------------------------------------------------------------------------------

       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,00928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinMercredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinMercredi.metadata = {
            title: 'autre',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinMercredi, 'click', pushpinClickedMercredi);

           //Add pushpin to the map.
           mapMercredi.entities.push(pinMercredi);

  // ---------------------------------------------------------------------------------------------------------------------------
  // ---------------------------------------------------------------------------------------------------------------------------
  // --------------------------------------------------------------------------------------------------------------------------- 


      var val = '47,43703290000'
      var lat = val.replace(",", ".");
      var val = '-2,08928090000'
      var lon = val.replace(",", ".");

       mapJeudi = new Microsoft.Maps.Map('#jeudi', {
         center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon))
       });
  
       //Create an infobox at the center of the map but don't show it.
       infoboxJeudi = new Microsoft.Maps.Infobox(mapJeudi.getCenter(), {
           visible: false
       });

       //Assign the infobox to a map instance.
       infoboxJeudi.setMap(mapJeudi);


       //-----------------------------------------------------------------------------------------
       
       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinJeudi  = new Microsoft.Maps.Pushpin(locs);
 
     pinJeudi.metadata = {
            title: 'Arnaud Jégoux',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinJeudi, 'click', pushpinClickedJeudi);

           //Add pushpin to the map.
           mapJeudi.entities.push(pinJeudi);


      //-----------------------------------------------------------------------------------------

       var val = '47,43803290000'
       var lat = val.replace(",", ".");
       var val = '-2,18928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinJeudi  = new Microsoft.Maps.Pushpin(locs);
 
     pinJeudi.metadata = {
            title: 'Marché de Ossé',
            description: 'place de la mairie 35410  Ossé'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinJeudi, 'click', pushpinClickedJeudi);

           //Add pushpin to the map.
           mapJeudi.entities.push(pinJeudi);


      //-----------------------------------------------------------------------------------------     
      
       var val = '47,48703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinJeudi  = new Microsoft.Maps.Pushpin(locs);
 
     pinJeudi.metadata = {
            title: 'marché de pontchat',
            description: '21 rue de Nantes 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinJeudi, 'click', pushpinClickedJeudi);

           //Add pushpin to the map.
           mapJeudi.entities.push(pinJeudi);
      
      //-----------------------------------------------------------------------------------------

       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,00928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinJeudi  = new Microsoft.Maps.Pushpin(locs);
 
     pinJeudi.metadata = {
            title: 'autre',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinJeudi, 'click', pushpinClickedJeudi);

           //Add pushpin to the map.
           mapJeudi.entities.push(pinJeudi);

  // ---------------------------------------------------------------------------------------------------------------------------
  // ---------------------------------------------------------------------------------------------------------------------------
  // --------------------------------------------------------------------------------------------------------------------------- 


      var val = '47,43703290000'
      var lat = val.replace(",", ".");
      var val = '-2,08928090000'
      var lon = val.replace(",", ".");

       mapVendredi = new Microsoft.Maps.Map('#vendredi', {
         center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon))
       });
  
       //Create an infobox at the center of the map but don't show it.
       infoboxVendredi = new Microsoft.Maps.Infobox(mapVendredi.getCenter(), {
           visible: false
       });

       //Assign the infobox to a map instance.
       infoboxVendredi.setMap(mapVendredi);


       //-----------------------------------------------------------------------------------------
       
       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinVendredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinVendredi.metadata = {
            title: 'Arnaud Jégoux',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinVendredi, 'click', pushpinClickedVendredi);

           //Add pushpin to the map.
           mapVendredi.entities.push(pinVendredi);


      //-----------------------------------------------------------------------------------------

       var val = '47,43803290000'
       var lat = val.replace(",", ".");
       var val = '-2,18928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinVendredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinVendredi.metadata = {
            title: 'Marché de Ossé',
            description: 'place de la mairie 35410  Ossé'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinVendredi, 'click', pushpinClickedVendredi);

           //Add pushpin to the map.
           mapVendredi.entities.push(pinVendredi);


      //-----------------------------------------------------------------------------------------     
      
       var val = '47,48703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinVendredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinVendredi.metadata = {
            title: 'marché de pontchat',
            description: '21 rue de Nantes 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinVendredi, 'click', pushpinClickedVendredi);

           //Add pushpin to the map.
           mapVendredi.entities.push(pinVendredi);
      
      //-----------------------------------------------------------------------------------------

       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,00928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinVendredi  = new Microsoft.Maps.Pushpin(locs);
 
     pinVendredi.metadata = {
            title: 'autre',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinVendredi, 'click', pushpinClickedVendredi);

           //Add pushpin to the map.
           mapVendredi.entities.push(pinVendredi);


  // ---------------------------------------------------------------------------------------------------------------------------
  // ---------------------------------------------------------------------------------------------------------------------------
  // --------------------------------------------------------------------------------------------------------------------------- 


      var val = '47,43703290000'
      var lat = val.replace(",", ".");
      var val = '-2,08928090000'
      var lon = val.replace(",", ".");

       mapSamedi = new Microsoft.Maps.Map('#samedi', {
         center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon))
       });
  
       //Create an infobox at the center of the map but don't show it.
       infoboxSamedi = new Microsoft.Maps.Infobox(mapSamedi.getCenter(), {
           visible: false
       });

       //Assign the infobox to a map instance.
       infoboxSamedi.setMap(mapSamedi);


       //-----------------------------------------------------------------------------------------
       
       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinSamedi  = new Microsoft.Maps.Pushpin(locs);
 
     pinSamedi.metadata = {
            title: 'Arnaud Jégoux',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinSamedi, 'click', pushpinClickedSamedi);

           //Add pushpin to the map.
           mapSamedi.entities.push(pinSamedi);


      //-----------------------------------------------------------------------------------------

       var val = '47,43803290000'
       var lat = val.replace(",", ".");
       var val = '-2,18928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinSamedi  = new Microsoft.Maps.Pushpin(locs);
 
     pinSamedi.metadata = {
            title: 'Marché de Ossé',
            description: 'place de la mairie 35410  Ossé'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinSamedi, 'click', pushpinClickedSamedi);

           //Add pushpin to the map.
           mapSamedi.entities.push(pinSamedi);


      //-----------------------------------------------------------------------------------------     
      
       var val = '47,48703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinSamedi  = new Microsoft.Maps.Pushpin(locs);
 
     pinSamedi.metadata = {
            title: 'marché de pontchat',
            description: '21 rue de Nantes 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinSamedi, 'click', pushpinClickedSamedi);

           //Add pushpin to the map.
           mapSamedi.entities.push(pinSamedi);
      
      //-----------------------------------------------------------------------------------------

       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,00928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinSamedi  = new Microsoft.Maps.Pushpin(locs);
 
     pinSamedi.metadata = {
            title: 'autre',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinSamedi, 'click', pushpinClickedSamedi);

           //Add pushpin to the map.
           mapSamedi.entities.push(pinSamedi);

  // ---------------------------------------------------------------------------------------------------------------------------
  // ---------------------------------------------------------------------------------------------------------------------------
  // --------------------------------------------------------------------------------------------------------------------------- 


      var val = '47,43703290000'
      var lat = val.replace(",", ".");
      var val = '-2,08928090000'
      var lon = val.replace(",", ".");

       mapDimanche = new Microsoft.Maps.Map('#dimanche', {
         center: new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon))
       });
  
       //Create an infobox at the center of the map but don't show it.
       infoboxDimanche = new Microsoft.Maps.Infobox(mapDimanche.getCenter(), {
           visible: false
       });

       //Assign the infobox to a map instance.
       infoboxDimanche.setMap(mapDimanche);


       //-----------------------------------------------------------------------------------------
       
       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinDimanche  = new Microsoft.Maps.Pushpin(locs);
 
     pinDimanche.metadata = {
            title: 'Arnaud Jégoux',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinDimanche, 'click', pushpinClickedDimanche);

           //Add pushpin to the map.
           mapDimanche.entities.push(pinDimanche);


      //-----------------------------------------------------------------------------------------

       var val = '47,43803290000'
       var lat = val.replace(",", ".");
       var val = '-2,18928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinDimanche  = new Microsoft.Maps.Pushpin(locs);
 
     pinDimanche.metadata = {
            title: 'Marché de Ossé',
            description: 'place de la mairie 35410  Ossé'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinDimanche, 'click', pushpinClickedDimanche);

           //Add pushpin to the map.
           mapDimanche.entities.push(pinDimanche);


      //-----------------------------------------------------------------------------------------     
      
       var val = '47,48703290000'
       var lat = val.replace(",", ".");
       var val = '-2,08928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinDimanche  = new Microsoft.Maps.Pushpin(locs);
 
     pinDimanche.metadata = {
            title: 'marché de pontchat',
            description: '21 rue de Nantes 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinDimanche, 'click', pushpinClickedDimanche);

           //Add pushpin to the map.
           mapDimanche.entities.push(pinDimanche);
      
      //-----------------------------------------------------------------------------------------

       var val = '47,43703290000'
       var lat = val.replace(",", ".");
       var val = '-2,00928090000'
       var lon = val.replace(",", ".");
       locs= new Microsoft.Maps.Location(parseFloat(lat), parseFloat(lon));
       var pinDimanche  = new Microsoft.Maps.Pushpin(locs);
 
     pinDimanche.metadata = {
            title: 'autre',
            description: '21 rue de Nantes, 44160 44160  Pontchateau'
          };

           //Add a click event handler to the pushpin.
           Microsoft.Maps.Events.addHandler(pinDimanche, 'click', pushpinClickedDimanche);

           //Add pushpin to the map.
           mapDimanche.entities.push(pinDimanche);

   }
   


   function pushpinClickedMardi(e) {
      //Make sure the infobox has metadata to display.
      if (e.target.metadata) {
          //Set the infobox options with the metadata of the pushpin.
          infoboxMardi.setOptions({
              location: e.target.getLocation(),
              title: e.target.metadata.title,
              description: e.target.metadata.description,
              visible: true
          });

           $('.carousel').carousel('pause');
      }
  }


   function pushpinClickedMercredi(e) {
      //Make sure the infobox has metadata to display.
      if (e.target.metadata) {
          //Set the infobox options with the metadata of the pushpin.
          infoboxMercredi.setOptions({
              location: e.target.getLocation(),
              title: e.target.metadata.title,
              description: e.target.metadata.description,
              visible: true
          });
           $('.carousel').carousel('pause');
      }
  }



   function pushpinClickedJeudi(e) {
      //Make sure the infobox has metadata to display.
      if (e.target.metadata) {
          //Set the infobox options with the metadata of the pushpin.
          infoboxJeudi.setOptions({
              location: e.target.getLocation(),
              title: e.target.metadata.title,
              description: e.target.metadata.description,
              visible: true
          });
           $('.carousel').carousel('pause');
      }
  }

   function pushpinClickedVendredi(e) {
      //Make sure the infobox has metadata to display.
      if (e.target.metadata) {
          //Set the infobox options with the metadata of the pushpin.
          infoboxVendredi.setOptions({
              location: e.target.getLocation(),
              title: e.target.metadata.title,
              description: e.target.metadata.description,
              visible: true
          });
           $('.carousel').carousel('pause');
      }
  }

   function pushpinClickedSamedi(e) {
      //Make sure the infobox has metadata to display.
      if (e.target.metadata) {
          //Set the infobox options with the metadata of the pushpin.
          infoboxSamedi.setOptions({
              location: e.target.getLocation(),
              title: e.target.metadata.title,
              description: e.target.metadata.description,
              visible: true
          });
           $('.carousel').carousel('pause');
      }
  }

   function pushpinClickedDimanche(e) {
      //Make sure the infobox has metadata to display.
      if (e.target.metadata) {
          //Set the infobox options with the metadata of the pushpin.
          infoboxDimanche.setOptions({
              location: e.target.getLocation(),
              title: e.target.metadata.title,
              description: e.target.metadata.description,
              visible: true
          });
           $('.carousel').carousel('pause');
      }
  }
