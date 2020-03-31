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