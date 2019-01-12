/* Añade un cero a la izquierda a los números de un solo dígito */
function pad(number) {
    if (number < 10)
        return '0' + number;
    else
	return number.toString();
}

/* Permite dar un formato a una fecha
   Por ejemplo para obtener formato tipo 01-01-2019, se utilizaría: 
   formatoFecha(date,'DD-MM-YYYY') */
function formatoFecha(date,formato){
    var dia = pad(date.getDate());
    var mes = pad((date.getMonth() + 1));
    var any = date.getFullYear().toString();
    return formato
	.replace('DD',dia)
	.replace('MM',mes)
	.replace('YYYY',any);
}

/* Transformación de fecha formato ISO a objeto Date */
function toDate(fechaiso){
    var campos = fechaiso.split("-");
    var dia = parseInt(campos[2]);
    var mes = parseInt(campos[1])-1;
    var any = parseInt(campos[0]);
    return new Date(any,mes,dia);
}

/* Fecha en campo #hidden (no visible) */
function fechaPagina(){
    return toDate($('#hidden').val());
}

/* Fecha en el campo de entrada del calendario */
function fechaCalendario(){
    return toDate($('#calendario').val());
}

/* Ir a la página de otra fecha */
/* Para días anteriores a la de comienzo del archivo
   se intenta cargar página de la versión antigua */
function cambiarFecha(date) {
    var url;
    if (date >= fechaInicioArchivo)
	url = '../' + formatoFecha(date,'YYYYMMDD') + '/' +
	      location.href.split("/").slice(-1);
    else
	url = 'http://172.24.139.32/autoinforme/auto_info_OK/Auto_informe/auto_informe_' + formatoFecha(date,'YYYY_MM_DD') + '/auto_info.html';
    window.location.href = url;
}

/* Obtener fecha desplazada agragando (o restando) días */
function fechaDesplazada(date, dias){
    var fecha = new Date(date.getTime());
    fecha.setDate(fecha.getDate() + dias);
    return fecha;
}

/* Fecha de inicio del archivo de imágenes */
var fechaInicioArchivo = new Date(2018,11,28);

/* Se inicia el calendario con la fecha del campo escondido */
$('#calendario').val($('#hidden').val())

/* Acción para botón fecha anterior */
$('#anterior').click(function(){
    var nuevaFecha = fechaDesplazada(fechaPagina(),-1);
    cambiarFecha(nuevaFecha);
});

/* Acción para botón fecha posterior */
$('#posterior').click(function(){
    var nuevaFecha = fechaDesplazada(fechaPagina(), 1);
    cambiarFecha(nuevaFecha);
});

/* Acción para botón Cambiar Día */
$('#cambiarDia').click(function(){
    cambiarFecha(fechaCalendario());
});


