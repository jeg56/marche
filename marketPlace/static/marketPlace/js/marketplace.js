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
  $("wait").show();
}


// Recherche par Categorie 
function searchCategorie() {
  var data = {
    searchCategorie: $('#id_categorie').val()
  };
  $.ajax({
      url: '/produit/categorie-filter/',
      data: data,
      type : 'GET',
      success : function(response){
        response.results.forEach(element => 
          $('#id_categorie').append($('<option>', {
            value: element.id,
            text:  element.label
          }))
        ) 
        $('#id_nom').val("")
        var element = document.getElementById("newNomProd");
        if(typeof(element) != 'undefined' && element != null){
            element.remove()
            document.getElementById("newPhotoProd").remove();
        }
      },
  });
}

// Recherche par produits 
function searchProduit(idProducteur) {
  var data = {
    searchCategorie:$('#id_categorie').val(),
    searchProduit: $('#id_nom').val(),
    idProducteur: idProducteur,
  };
  $.ajax({
      url: '/produit/produit-filter/',
      data: data,
      type : 'GET',
      success : function(response,){
        var nom_id="id_nom"
        $('#'+nom_id+ "autocomplete-list").remove().end()
        var element = document.getElementById("newNomProd");
        if(typeof(element) != 'undefined' && element != null){
            element.remove()
            document.getElementById("newPhotoProd").remove();
        }
      

        a = document.createElement("DIV");
        a.setAttribute("id", nom_id + "autocomplete-list");
        a.setAttribute("class", "form-control autocomplete-items  taille");
        document.getElementById(nom_id).parentNode.appendChild(a);
        response.results.forEach(element => {
            /*create a DIV element for each matching element:*/
            b = document.createElement("DIV");
            
            /*make the matching letters bold:*/
            b.innerHTML = "<strong>" + element.nom.substr(0,$('#'+nom_id).val().length)+ "</strong>";
            b.innerHTML += element.nom.substr($('#'+nom_id).val().length);
            b.innerHTML += "<input type='hidden' value='" + element.nom + "'>";
            b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              $('#'+nom_id).val(this.getElementsByTagName("input")[0].value) 
            });
            a.appendChild(b); 
          }
        )

        // -------------------------------------------------------------------------------------------
        // -------------------------------------------------------------------------------------------
  
        b = document.createElement("DIV");
         
        b.innerHTML="<span style='color:red'> Pour ajouter un nouveau produit... </span>"
        b.innerHTML += "<input type='hidden' value='Autre'>";
        b.addEventListener("click", function(e) {
              $('#'+nom_id).val( this.getElementsByTagName("input")[0].value)
             
            
              getNameProd = document.createElement("DIV");
              getNameProd.innerHTML +='<div><label> Nom du produit : </label><input id="newNomProd" name="newNomProd" type="text" class="form-control" placeholder="Entrer le nom du nouveau produit"></div>'
              getNameProd.innerHTML +='<div><label> Photo : </label> <input id="newPhotoProd" name="newPhotoProd" class="newProd" type="file"  value="Ajouter une photo"></div>'
        
              a.after(getNameProd )


          });

        a.appendChild(b);

      // -------------------------------------------------------------------------------------------
      // -------------------------------------------------------------------------------------------

      },
  });
}

// Vide toutes les listes si on click a coté 
document.addEventListener("click", function (e) {
  $("#id_nomautocomplete-list").remove().end()
});


