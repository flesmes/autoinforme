/* Cambiar fecha */

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

function toDate(fechaiso){
    var campos = fechaiso.split("-");
    var dia = parseInt(campos[2]);
    var mes = parseInt(campos[1])-1;
    var any = parseInt(campos[0]);
    return new Date(any,mes,dia);
}

function fechaPagina(){
    return toDate($('#hidden').val());
}

function fechaCalendario(){
    return toDate($('#calendario').val());
}

function cambiarFecha(date) {
    var url;
    console.log(date)
    console.log(fechaInicioArchivo)
    console.log(date >= fechaInicioArchivo)
    if (date >= fechaInicioArchivo)
	url = '../' + formatoFecha(date,'YYYYMMDD') + '/' +
	      location.href.split("/").slice(-1);
    else
	url = 'http://172.24.139.32/autoinforme/auto_info_OK/Auto_informe/auto_informe_' + formatoFecha(date,'YYYY_MM_DD') + '/auto_info.html';
    window.location.href = url;
}

function moverFecha(date, dias){
    var nuevaFecha = new Date(date.getTime());
    nuevaFecha.setDate(nuevaFecha.getDate() + dias);
    cambiarFecha(nuevaFecha);
}

var fechaInicioArchivo = new Date(2018,11,28);

$('#calendario').val($('#hidden').val())

$('#anterior').click(function(){
    moverFecha(fechaPagina(),-1);
});

$('#posterior').click(function(){
   moverFecha(fechaPagina(),1)
});

$('#cambiarDia').click(function(){
    cambiarFecha(fechaCalendario());
});


