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
        var element = document.getElementById("newProd");
        if(typeof(element) != 'undefined' && element != null){
            element.remove()
            document.getElementById("photoProd").remove();
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
        var element = document.getElementById("newProd");
        if(typeof(element) != 'undefined' && element != null){
            element.remove()
            document.getElementById("photoProd").remove();
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
              getNameProd.innerHTML +='<div><label> Nom du produit : </label><input id="newProd" class="form-control" placeholder="Entrer le nom du nouveau produit"></div>'
              getNameProd.innerHTML +='<div><label> Photo : </label> <input id="photoProd" class="newProd" type="file"  value="Ajouter une photo"></div>'
        
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



  
// ----------------------------------------------------------------------------------------------------------------
// ----------------------------------------------------------------------------------------------------------------

var listElInit=[]
var listElFin=[]
$(function() {
  $("#sortable").sortable({
    stop: function(evt, ui) {
      listElFin=[]
      document.getElementsByName('imgDragable').forEach(elt=>{
          listElFin.push(elt.getAttribute("value"))
        })
        validOrdreProduit()
      }
    }
  );
  $("#sortable").disableSelection();
  searchCategorie();
  document.getElementsByName('imgDragable').forEach(elt=>{
    listElInit.push(elt.getAttribute("value"))
  })
  listElFin=listElInit
  document.getElementById("btn-valid-produit-producteur").style.display = 'none';
  
});


function validOrdreProduit(){
  if( arrIdentical(listElInit,listElFin)){
    document.getElementById("btn-valid-produit-producteur").style.display = 'none';
    document.getElementById('input-ordre-produit-producteur').value=''
  }else{
    document.getElementById("btn-valid-produit-producteur").style.display = 'block';
    document.getElementById('input-ordre-produit-producteur').value=listElFin
  }
}
function arrIdentical(a1, a2) {
  var i = a1.length;
  if (i != a2.length) return false;
  while (i--) {
      if (a1[i] !== a2[i]) return false;
  }
  return true;
}


// ----------------------------------------------------------------------------------------------------------------
// ----------------------------------------------------------------------------------------------------------------

function getPos(e){
  x=e.clientX;
  y=e.clientY;
  cursor="Your Mouse Position Is : " + x + " and " + y ;
  console.log(cursor)
}