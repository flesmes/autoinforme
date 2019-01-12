var nImagenes = 24;
var actual = 0;
var intervalo = 500; // 500 ms
var animacion = false;
var animacionId;
var imgAnimacion = $('img.animacion');

/* Cambia a las imagenes de índice i */
function cambiarImg(i) {
    var nombre;
    nombre = (i<10 ? 'RAD0' : 'RAD') + i + 'NAC00_RA2D.PNG';
    $('#radar-2d').attr('src',nombre);
    nombre = (i<10 ? 'RAD0' : 'RAD') + i + 'NAC00_ACC.PNG';
    $('#radar-acc').attr('src',nombre);
}

/* Cambia a la imagen siguiente */
function siguiente() {
    actual = actual == nImagenes-1 ? 0 : actual+1;
    cambiarImg(actual);
}

/* Acción para pasar a la imagen siguiente */
/* Solo si no hay animación en marcha */
function siguienteListener() {
    if (! animacion) siguiente();
}

/* Cambia a la imagen anterior */
function anterior() {
    actual = actual==0 ? nImagenes-1 : actual-1;
    cambiarImg(actual);
}

/* Acción para pasar a la imagen anterior */
/* Solo si no hay animación en marcha */
function anteriorListener() {
    if (! animacion) anterior();
}

/* Acción de animación */
function animarListener() {
    if (! animacion) {
	animacion = true;
	animacionId = setInterval(siguiente, intervalo);
    }
}

/* Acción de parar la animación */
function pararListener() {
    if (animacion) {
	animacion = false;
	clearInterval(animacionId);
    }
}

/* Acciones asignadas a cada botón */

$('button.prev').click(anteriorListener);

$('button.siguiente').click(siguienteListener);

$('button.animar').click(animarListener);

$('button.parar').click(pararListener);


