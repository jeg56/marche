



function shownHidden(e){
    if (e.checked) {
        document.getElementById('hor'+e.name).style.display = 'inline';
    } else {
        document.getElementById('hor'+e.name).style.display = 'none';
    }
}



$(function () {
    var jourSemaine=['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']

    jourSemaine.forEach(e => {
        if ($('#'+e+':checkbox').is(':checked')) {
            $('#hor'+e+'').css("display","inline")
        } else {
            $('#hor'+e+'').css("display","none")
        }

    });
});