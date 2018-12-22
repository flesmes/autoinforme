/* Fecha en formato YYYYMMDD */
function fechaFormato(fecha) {
    var dia = fecha.getDate();
    var diaStr = fecha.getDate().toString();
    if ( dia < 10) 
	diaStr = "0" + diaStr;
    var mesStr = (fecha.getMonth() + 1).toString();
    var anyStr = fecha.getFullYear().toString();
    return anyStr + mesStr + diaStr;
}

var fecha = new Date();           /* Hoy */
fecha.setDate(fecha.getDate()-1); /* Ayer */
var url = 'archivo/' + fechaFormato(fecha) + '/sinoptica.html';
window.location.replace(url);
