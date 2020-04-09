

$(document).ready(function() {
    $('#francemap').vectorMap({
        map: 'france_fr',
        hoverOpacity: 0.5,
        hoverColor: false,
        backgroundColor: "#ffffff",
        colors: couleurs,
        borderColor: "#000000",
        selectedColor: "#EC0000",
        enableZoom: false,
        showTooltip: true,
        onRegionClick: function(element, code, region)
        {
            var data = {
                searchCP:code,
              };
            
              $.ajax({
                  url: '/producteur/market-filter-cp/',
                  data: data,
                  type : 'GET',
                  success : function(response){

                    dataCoordAdresse=response
                    
                    var mapScriptUrl = 'https://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=Aj-CW4KKZ2QbFVCuOEKVg7PpUsZvMYhJaKLY226BDjRkw-s4tJCKsv0onicoVP5d';
                    var script = document.createElement("script");
                    script.setAttribute('defer', '');
                    script.setAttribute('async', '');
                    script.setAttribute("type", "text/javascript");
                    script.setAttribute("src", mapScriptUrl);
                    document.body.appendChild(script);
 

                  },
              });



        }
    });
});