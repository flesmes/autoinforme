/* Cambiar pasada */

/* Cambia el valor el estilo "display" para la sección de índice "i" */
function displaySection(i,style){
    var selector = "#s" + i;
    var section = document.querySelector(selector);
    section.style.display = style;
}

/* Cambio de pasada. Se esconde la antigua sección activa 
   y se muestra la nueva */
function changeActive(){
    displaySection(activo,"none");
    activo = widget.value;
    displaySection(activo,"block");
}

/* Inicialmente la pasada activa es la primera */
/* Se muestra la pasada activa, las demás se esconden */
var activo = 1; 
for (var i = 1; i <= 3; i++) {
     displaySection(i,"none"); 
} 
displaySection(activo,"block");

/* Acción para el selector de pasada */
var widget = document.querySelector("#choose");
widget.addEventListener("change",changeActive);
