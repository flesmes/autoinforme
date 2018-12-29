# -*- coding: latin-1 -*-

import datetime
import PIL.Image
import os
import re
import requests
import shutil

import config

def descargarURL(remoto,local):
    r = requests.get(remoto)
    #print
    print('descargado ' + remoto)
    #print r.headers;
    #print r.request.headers
    lfile = open(local, 'wb')
    lfile.write(r.content)
    lfile.close()
    
def redimensionar(path, anchura):
    img_ini = PIL.Image.open(path).convert('RGB')
    (anchura_ini,altura_ini) = img_ini.size
    zoom = float(anchura) / float(anchura_ini)
    altura = int(altura_ini * zoom )
    img_redim = img_ini.resize((anchura,altura), PIL.Image.ANTIALIAS)
    os.remove(path)

    # Aparece un error al guardar algunos gif,
    # Se guardarán como png
    extension = re.search('\.[^.]*$',path).group(0)
    nombre = path[:-len(extension)]
    if extension == '.gif' or extension == '.GIF':
        extension = '.png'

    img_redim.save(nombre+extension)

def tieneDirectorio(path):
    return len(path.split('/')) > 1
    
def descargarImagenes( images, fecha):

    dmas1 = fecha + datetime.timedelta(1)
    dmas2 = fecha + datetime.timedelta(2)

    directoriosArchivo = \
      [config.pathArchivo + '/' + dia.strftime('%Y%m%d') \
       for dia in [fecha, dmas1, dmas2]]
    #default
    dirArchivoFecha = directoriosArchivo[0]
    
    # Si no existen los directorios de archivo, los crea
    for dir in directoriosArchivo:
        if not os.path.exists(dir):
            os.mkdir(dir)

    # Para cada imagen;
    # descarga la imagen
    # redimensiona la imagen
    
    for image in images:

        if tieneDirectorio(image.localfile):
            local = config.pathArchivo + '/' + image.localfile
        else:
            local = dirArchivoFecha + '/' + image.localfile

        try:
            descargarURL(image.remotefile, local);
            #print('Descargado {}'.format(image.remotefile))
        except:
            print('Fallo descargando {}'.
                  format(image.remotefile))
            shutil.copyfile(config.pathTemplates + '/nodisponibler.png',
                            local)
        redimensionar(local, image.width)
        


