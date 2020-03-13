// Recherche par ville 
function searchVille() {
    var data = {
        searchVille: $('#id_ville').val(),
        searchCP: $('#id_cp').val(),
    };
 
    $.ajax({
        url: '/ville-autocomplete/',
        data: data,
        type : 'GET',
        success : function(response){
            $( "#id_ville" ).autocomplete({
              source: response
            });
        },

    });
}


// Recherche par cp 
function searchCP() {
  var data = {
    searchVille: $('#id_ville').val(),
    searchCP: $('#id_cp').val(),
  };

  $.ajax({
      url: '/cp-autocomplete/',
      data: data,
      type : 'GET',
      success : function(response){
          $( "#id_cp" ).autocomplete({
            source: response
          });
      },

  });
}

function validationForm() {
 
  $("#myModal").show();
}
