#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import datetime
import jinja2
import os
import sys

import config

class Pagina:
  def __init__(self,nombre,descripcion):
      self.nombre = nombre
      self.descripcion = descripcion

paginas = [Pagina('sinoptica.html', u'Situación sinóptica'),
           Pagina('precipitacion.html', u'Precipitación'),
           Pagina('nieve.html', 'Nieve'),
           Pagina('viento.html', 'Viento'),
           Pagina('temperatura.html', 'Temperatura'),
           Pagina('radar.html', 'Radar'),
           Pagina('nubesbajas.html', 'Nubes bajas')]

class Fecha:
  def __init__(self,date):
    self.dia = date.strftime('%d')
    self.mes = date.strftime('%m')
    self.any = date.strftime('%Y')

def fechaNatural(fecha):
    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril',
             5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto',
             9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}
    dia = fecha.day
    mes = fecha.month
    anio = fecha.year
    return '{} de {} de {}'.format(dia,meses[mes],anio)

def generar(fecha):
    jinjaEnv = jinja2.Environment(
        loader = jinja2.FileSystemLoader(config.pathTemplates),
        autoescape = jinja2.select_autoescape(['html']),
        trim_blocks = True,
        lstrip_blocks = True)

    # Directorio para guardar imagenes, basado en la fecha
    # Si no existe lo crea
    pathArchivoFecha = config.pathArchivo + '/' + fecha.strftime('%Y%m%d')
    print('Los archivos html se guardarán en ' + pathArchivoFecha)
    if not os.path.exists(pathArchivoFecha):
        os.mkdir(pathArchivoFecha)

    for pagina in paginas:

        template = jinjaEnv.get_template(pagina.nombre)
        enlaces = [enlace for enlace in paginas if enlace != pagina]
        variables = {'fecha': Fecha(fecha),
                     'fechaNatural': fechaNatural(fecha),
                     'fechaPosterior': Fecha(fecha + datetime.timedelta(1)),
                     'enlaces': enlaces}
        output = template.render(variables)
        
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

# Argumentos: Año mes dia (en número)
# Sin argumentos: Fecha de ayer
# Con argumentos: Fecha indicada
if __name__=="__main__":
    fecha = getFecha(sys.argv)
    generar(fecha)

