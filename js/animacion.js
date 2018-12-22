var nImagenes = 24;
var actual = 0;
var intervalo = 500; // 500 ms
var animacion = false;
var animacionId;
var imgAnimacion = $('img.animacion');

function cambiarImg(i) {
    if (imgAnimacion.hasClass('radar'))
	var nombre = (i<10 ? 'RAD0' : 'RAD') + i + 'NAC00_RA2D.PNG';
    if (imgAnimacion.hasClass('bajas'))
	var nombre = (i<10 ? 'SAT0' : 'SAT') + i + 'NWCSAF_MNP100_CT_Bajas.PNG';
    imgAnimacion.attr('src',nombre);
}

function siguiente() {
    actual = actual == nImagenes-1 ? 0 : actual+1;
    cambiarImg(actual);
}

function siguienteListener() {
    if (! animacion) siguiente();
}

function anterior() {
    actual = actual==0 ? nImagenes-1 : actual-1;
    cambiarImg(actual);
}

function anteriorListener() {
    if (! animacion) anterior();
}

function animarListener() {
    if (! animacion) {
	animacion = true;
	animacionId = setInterval(siguiente, intervalo);
    }
}

function pararListener() {
    if (animacion) {
	animacion = false;
	clearInterval(animacionId);
    }
}

$('#prev').click(anteriorListener);

$('#siguiente').click(siguienteListener);

$('#animar').click(animarListener);

$('#parar').click(pararListener);


