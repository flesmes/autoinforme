import datetime
import PIL.Image
import os
import re
import requests
import shutil

import config

# descargar URL en archivo
def descargarURL(url,archivo):
    r = requests.get(url)
    print('descargado ' + url)
    lfile = open(archivo, 'wb')
    lfile.write(r.content)
    lfile.close()

# redimensionar imagen para anchura determinada,
# sin cambiar relación anchura-altura
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

# path incluye directorio  
def tieneDirectorio(path):
    return len(path.split('/')) > 1

# descargar imagenes
# images - lista de archivos de imagenes
# fecha - día del informe
def descargarImagenes( images, fechaD):

    # La mayor parte de las imágenes se guardan en la
    # carpeta correspondiente al día D (día del informe)
    # Pero algunas se guardan en las carpetas del día D+1 y D+2
    
    fechaD1 = fechaD + datetime.timedelta(1)
    fechaD2 = fechaD + datetime.timedelta(2)
   
    directoriosArchivo = \
      [config.pathArchivo + '/' + dia.strftime('%Y%m%d') \
       for dia in [fechaD, fechaD1, fechaD2]]
    dirArchivoFechaD = directoriosArchivo[0]
    print('Las imagenes se guardaran en ' + dirArchivoFechaD)
    
    # Si no existen los directorios de archivo, los crea
    for dir in directoriosArchivo:
        if not os.path.exists(dir):
            os.mkdir(dir)

    # Para cada imagen;
    # descarga la imagen
    # redimensiona la imagen
    
    for image in images:

        # Las imagenes que se archivan en la carpeta del día D
        # no llevan el nombre del directorio en el path de la imagen.
        # Las que se archivan el directorio del día D+1 o D+2, sí
        if tieneDirectorio(image.localfile):
            local = config.pathArchivo + '/' + image.localfile
        else:
            local = dirArchivoFechaD + '/' + image.localfile

        try:
            descargarURL(image.remotefile, local);
            #print('Descargado {}'.format(image.remotefile))
            redimensionar(local, image.width)
        except:
            print('Fallo descargando {}'.
                  format(image.remotefile))
            shutil.copyfile(config.pathTemplates + '/nodisponibler.png',
                            local)
        


