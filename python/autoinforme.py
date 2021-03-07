#!/usr/bin/python3

import datetime
import sys

import descarga
import html

# Obtener fecha a partir de los argumentos (si los hay)
# o si no la fecha de ayer
# Sin argumentos: Fecha de ayer
# Con argumentos: Fecha indicada
# Argumentos: Año mes dia (en número)

def getFecha(args):
    if len(args) == 1:
        return datetime.date.today() - datetime.timedelta(1);
    elif len(args) == 4:
        return datetime.date(int(args[1]), int(args[2]), int(args[3]))
    else:
        sys.exit(1);

fecha = getFecha(sys.argv)

descarga.descargarImagenes(fecha)

html.generar(fecha);
        


