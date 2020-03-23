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



  
// ----------------------------------------------------------------------------------------------------------------
// ----------------------------------------------------------------------------------------------------------------

var listElInit=[]
var listElFin=[]

$(function() {
  $("#sortable").sortable({
 
    start: function(evt, ui) {
      document.getElementById("imgPoubelle").style.display = 'block';

      },
    stop: function(evt, ui) {
      listElFin=[]
      document.getElementsByName('imgDragable').forEach(elt=>{
          listElFin.push(elt.getAttribute("value"))
        })
        validOrdreProduit()
        document.getElementById("imgPoubelle").style.display = 'none';

        
        if (isInPoubelle(evt)){
          $("#Produit_"+produit_id).css("border", "#999999 solid 1px");
            $.ajax({
      
              url: '/produit/del/'+producteur_id+'/'+produit_id,
              type : 'GET',
              success : function(response){
                // ------------------------------------------------------------
                $("#Produit_"+response.results).remove();
                // ------------------------------------------------------------
              },
              error: function(XMLHttpRequest, textStatus, errorThrown) { 
                console.log("Status: " + textStatus); 
                console.log("Error: " + errorThrown); 
            }  
          });
          produit_id=''
       
          
        }else{
    
          $("#Produit_"+produit_id).css("border", "#999999 solid 1px");
   
          produit_id=''
        }
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

var produit_id=''
var producteur_id=''
function initIdGlobal(id,idProd){

  produit_id=id
  producteur_id=idProd
  console.log(producteur_id)
  console.log(produit_id)
}


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





function isInPoubelle(e){
  x=e.clientX;
  y=e.clientY;
  isInPoubelleFlag=false
  if (y<200){
    var element =  document.getElementsByClassName('imgPoubelle');
    if (typeof(element) != 'undefined' && element != null)
    {
      isInPoubelleFlag=true
      $("#Produit_"+produit_id).css("border", "red solid 2px");
    }
    
  }
  return isInPoubelleFlag
}

$(function() {
  document.getElementsByName("imgDragable").forEach(elmt=>{
    $(elmt).hover(function(event){
      $(this).css("cursor", "webkit-grab");
      $(this).css("cursor","grab");
      $(this).css("border", "black solid 2px");
      $(this).css("background-color",'white');
       }, function(){
        $(this).css("cursor", "default");
        $(this).css("border", "#999999 solid 1px");
        $(this).css("background-color",'white');

    });
  })
  
  $("#imgPoubelle").hover(function(event){
    $(this).css("cursor", "webkit-grab");
    $(this).css("cursor","grab");
    $(this).css("border", "green solid 2px");
    $(this).css("background-color",'green');
     }, function(){
      $(this).css("cursor", "default");
      $(this).css("border", "#999999 solid 1px");
      $(this).css("background-color",'green');

});
});