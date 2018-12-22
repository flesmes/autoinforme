#!/usr/bin/python
# -*- coding: latin-1 -*-

import datetime
import sys

import descarga
import html
import init

def getFecha(args):
    if len(args) == 1:
        return datetime.date.today() - datetime.timedelta(1);
    elif len(args) == 4:
        return datetime.date(int(args[1]), int(args[2]), int(args[3]))
    else:
        sys.exit(1);

# Argumentos: Año mes dia (en número)
# Sin argumentos: Fecha de ayer
# Con argumentos: Fecha indicada
fecha = getFecha(sys.argv)

imagenes = init.listaImagenes(fecha)
descarga.descargarImagenes(imagenes, fecha)

html.generar(fecha);
        


