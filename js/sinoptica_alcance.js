/* Event listener para el control del alcance de situación sinóptica.
    - Presión y nubosidad
    - TZ 850 hPa
    - TZ 500 hPa
    - TZ 300 hPa
*/
$("#control_alcance").change( evento => {
    let alcance = evento.target.value
    $("#imagen_prenub").attr("src", `MOD00CES10${alcance}NUB.1.png`)
    $("#imagen_tz850").attr("src", `MOD00CES10${alcance}TZ_850.1.png`)
    $("#imagen_tz500").attr("src", `MOD00CES10${alcance}TZ_500.1.png`)
    $("#imagen_tz300").attr("src", `MOD00CES10${alcance}TZ_300.1.png`)
 })    
