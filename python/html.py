#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import datetime
import jinja2
import os
import sys

import boletines
import config

class Pagina:
  def __init__(self,nombre,descripcion):
      self.nombre = nombre
      self.descripcion = descripcion

paginas = [Pagina('sinoptica.html', u'Situación sinóptica'),
           Pagina('precipitacion.html', u'Precipitación'),
           Pagina('nieve.html', 'Nieve'),
           Pagina('rayos.html', 'Rayos'),
           Pagina('viento.html', 'Viento'),
           Pagina('temperatura.html', 'Temperatura'),
           Pagina('efi.html', 'EFIs'),
           Pagina('radar.html', 'Radar'),
           Pagina('boletines.html', 'Boletines'),
          ]

class Fecha:
  def __init__(self,date):
    self.dia = date.strftime('%d')
    self.mes = date.strftime('%m')
    self.any = date.strftime('%Y')

# fecha en formato "Dia de Mes de Año"
def fechaNatural(fecha):
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril',
             5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto',
             9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
    dia = fecha.day
    mes = fecha.month
    anio = fecha.year
    return '{} de {} de {}'.format(dia,meses[mes],anio)

# generar archivos HTML  
def generar(fecha):
  
    jinjaEnv = jinja2.Environment(
        loader = jinja2.FileSystemLoader(config.pathTemplates),
        trim_blocks = True,
        lstrip_blocks = True)

    # Directorio para guardar imagenes, basado en la fecha
    # Si no existe lo crea
    pathArchivoFecha = config.pathArchivo + '/' + fecha.strftime('%Y%m%d')
    print('Los archivos html se guardaran en ' + pathArchivoFecha)
    if not os.path.exists(pathArchivoFecha):
        os.mkdir(pathArchivoFecha)

    variables = {}
    variables['fecha'] = Fecha(fecha)
    variables['fechaNatural'] = fechaNatural(fecha)
    variables['fechaPosterior'] = Fecha(fecha + datetime.timedelta(1))

    # Descargar boletines
    for area in ['cat', 'ara', 'val', 'bal']:
        for alcance in [1,2]:
            key = 'bol{}{}'.format(area,alcance)
            variables[key] = boletines.descargarPrediccion(fecha,alcance,area)

    variables['guia'] = boletines.descargarGuia(fecha)
        
    for pagina in paginas:

        template = jinjaEnv.get_template(pagina.nombre)

        # Filtrado de enlaces.
        # Las páginas no deben incluir enlaces a sí mismas
        variables['enlaces'] = \
            [enlace for enlace in paginas if enlace != pagina]

        # Generación del contenido de la página a partir de una plantilla
        output = template.render(variables)

        # El contenido de la página se guarda en archivo
        destino = pathArchivoFecha + '/' + pagina.nombre
        file = codecs.open(destino,'w',encoding='utf-8')
        file.write(output)
        file.close()

        print('Generado ' + pagina.nombre)
       
        
def getFecha(args):
    if len(args) == 1:
        return datetime.date.today() - datetime.timedelta(1);
    elif len(args) == 4:
        return datetime.date(int(args[1]), int(args[2]), int(args[3]))
    else:
        sys.exit(1);

# Este script se puede utilizar como módulo importado o como main.
# Si se utiliza como main, la fecha se obtiene 
# a partir de los argumentos (si los hay)
# o si no, por defecto, de la fecha de ayer
# Argumentos: Año mes dia (en número)
# Sin argumentos: Fecha de ayer
# Con argumentos: Fecha indicada

if __name__=="__main__":
    fecha = getFecha(sys.argv)
    generar(fecha)

