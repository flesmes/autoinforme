#!/usr/bin/python
# -*- coding: latin-1 -*-

import datetime
import os
import sys

import config

def formatoFecha(fecha):
    dia = fecha.day
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril',
             5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto',
             9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
    mes = meses[fecha.month]
    anio = fecha.year
    return '{} de {} de {}'.format(dia,mes,anio)

def generar(fecha):
    files = ['precipitacion.html',
             'sinoptica.html',
             'nieve.html',
             'viento.html',
             'temperatura.html',
             'radar.html',
             'nubesbajas.html']

    # Directorio para guardar imagenes, basado en la fecha
    # Si no existe lo crea
    pathArchivoFecha = config.pathArchivo + '/' + fecha.strftime('%Y%m%d')
    print('path archivo ' + pathArchivoFecha)
    if not os.path.exists(pathArchivoFecha):
        os.mkdir(pathArchivoFecha)

    for file in files:
        print(file)
        origen = config.pathTemplates + '/' + file
        destino = pathArchivoFecha + '/' + file
        date = 'new Date({},{},{})'.format(fecha.year,
                                           fecha.month - 1,
                                           fecha.day)
        out = open(destino,'w')
        print(destino)
        for line in open(origen):
            line = line.replace('<h1>Informe del</h1>',
                                '<h1>Informe del ' + formatoFecha(fecha) + '</h1>')
            line = line.replace('<script>date=</script>',
                                '<script>date='+date+'</script>')
            out.write(line)
        out.close()
        
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
if __name__=="__main__":
    fecha = getFecha(sys.argv)
    generar(fecha)

