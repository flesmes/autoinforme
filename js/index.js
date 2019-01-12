function pad(number) {
    if (number < 10)
        return '0' + number;
    else
	return number.toString();
}

function formatoFecha(date,formato){
    var dia = pad(date.getDate());
    var mes = pad((date.getMonth() + 1));
    var any = date.getFullYear().toString();
    return formato
	.replace('DD',dia)
	.replace('MM',mes)
	.replace('YYYY',any);
}

function existeURL(url) {
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status != 404;
}

var fecha = new Date(); // Hoy
console.log(fecha)
var url;

/* Encuentra la url de la página para el día anterior
   Comprueba si la página existe
   Si no existe vuelve a probar sucesivamente con días anteriores
*/
while (true) {
    fecha.setDate(fecha.getDate()-1); // Día anterior
    url = 'archivo/' + formatoFecha(fecha,'YYYYMMDD') + '/sinoptica.html';
    if (existeURL(url)) break;
}

window.location.replace(url);
