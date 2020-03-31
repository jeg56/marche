
$( function() {
    var availableTags = [
      " Ossé ",
      "Chateaugiron",
      "Rennes"
    ];


    $( "#tags" ).autocomplete({
      source: function (request, response) {
        var i=0
        $.getJSON("../json/commune.json?term=" + request.term, function (data) {
            response($.map(data.Communes, function (value, key) {
                
                var re = $.ui.autocomplete.escapeRegex(request.term);
                var matcher = new RegExp( "^" + re, "i" );

                if(matcher.test(value) && i<=10){
                    i=i+1
                     return {
                    label: value,
                    value: 'Ville sélectionnée : '+value
                };
                }

            }));
        });
    }
    });
$( "#recherche" ).autocomplete({
      source: availableTags
  } );


})