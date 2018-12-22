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



function toDate(fecha){
    var campos =  fecha.split("-");
    var dia = parseInt(campos[2]);
    var mes = parseInt(campos[1])-1;
    var any = parseInt(campos[0]);
    return new Date(any,mes,dia);
}

function formatoDate(date){
    var dia = pad(date.getDate());
    var mes = pad((date.getMonth() + 1));
    var any = date.getFullYear().toString();
    return any + mes + dia;
}

function formatoAntiguo(date){
    var dia = pad(date.getDate());
    var mes = pad((date.getMonth() + 1));
    var any = date.getFullYear().toString();
    return any + '_' + mes + '_' + dia;
}

function cambiarFecha(date) {
    var url;
    if (date - fechaInicioArchivo >= 0)
	url = '../' + formatoFecha(date,'YYYYMMDD') + '/' + file;
    else
	url = 'http://172.24.139.32/autoinforme/auto_info_OK/Auto_informe/auto_informe_' + formatoFecha(date,'YYYY_MM_DD') + '/auto_info.html';
    window.location.href = url;
}

var botonAnterior = document.querySelector('#anterior');
botonAnterior.addEventListener("click", function(){
    var dateAnterior = new Date(date.getTime());
    dateAnterior.setDate(date.getDate()-1);
    cambiarFecha(dateAnterior);
});

var botonPosterior = document.querySelector('#posterior');
botonPosterior.addEventListener("click", function(){
    var datePosterior = new Date(date.getTime());
    datePosterior.setDate(date.getDate()+1);
    cambiarFecha(datePosterior);
});

function nuevaFecha(){
    console.log("clickLoad");
    console.log(toDate(calendario.value));
    cambiarFecha(toDate(calendario.value));
}

var fechaInicioArchivo = new Date(2018,11,14);

var calendario = document.querySelector('#calenda');
calendario.value = formatoFecha(date,'YYYY-MM-DD')
calendario.addEventListener('change', nuevaFecha);


