/* Cambiar pasada */

function displaySection(i,style){
    var selector = "#s" + i;
    var section = document.querySelector(selector);
    section.style.display = style;
}

function changeActive(){
    displaySection(activo,"none");
    activo = widget.value;
    displaySection(activo,"block");
}


var activo = 1; 
for (var i = 1; i <= 3; i++) {
     displaySection(i,"none"); 
} 
displaySection(activo,"block");

var widget = document.querySelector("#choose");
widget.addEventListener("change",changeActive);
