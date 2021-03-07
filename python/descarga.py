import datetime
import PIL.Image
import os, os.path
import re
import requests
import shutil

import bigdata
import config
import init

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
def descargarImagenesVIM(fechaD):

    # La mayor parte de las imágenes se guardan en la
    # carpeta correspondiente al día D (día del informe)
    # Pero algunas se guardan en las carpetas del día D+1 y D+2
    
    fechaD1 = fechaD + datetime.timedelta(1)
    fechaD2 = fechaD + datetime.timedelta(2)
    dias = [dia.strftime('%Y%m%d') for dia in [fechaD, fechaD1, fechaD2]]

    baseArchivo = os.path.join( config.wwwPath, 'archivo')
    directoriosArchivo = [os.path.join(baseArchivo, dia) for dia in dias] 
    dirArchivoFechaD = directoriosArchivo[0]
    print('Las imagenes se guardaran en ' + dirArchivoFechaD)
    
    # Si no existen los directorios de archivo, los crea
    for dir in directoriosArchivo:
        if not os.path.exists(dir):
            os.mkdir(dir)

    imagenes = init.listaImagenes(fechaD)

# Para cada imagen;
    # descarga la imagen
    # redimensiona la imagen
    
    for image in imagenes:

        # Path para las imagenes
        # Para las del dia D, image.localFile solo incluye el
        # nombre del fichero.
        # Añadir el path del directorio que las contiene
        # Para las del dia D+1 y D+2, el nombre image.localFile
        # contiene el directorio con la fecha correspondiente.
        # Detectar que el nombre incluye el directorio (tieneDirectorio)
        # y añadir el path del directorio base de archivo
        if tieneDirectorio(image.localfile):
            imageLocalPath = os.path.join( baseArchivo, image.localfile)
        else:
            imageLocalPath = os.path.join( dirArchivoFechaD,
                                           image.localfile)

        try:
            descargarURL(image.remotefile, imageLocalPath);
            #print('Descargado {}'.format(image.remotefile))
            redimensionar(imageLocalPath, image.width)
        except:
            print('Fallo descargando {}'.
                  format(image.remotefile))
            noDisponible = os.path.join( config.srcPath,
                                         'templates',
                                         'nodisponibler.png')
            shutil.copyfile(noDisponible, imageLocalPath)

# Descarga de imágenes de estimación por radar de acumulación de precipitación en 24 horas
def descargarImagenesBigData(fecha):

    # La fecha para la URL es la del día siguiente (a las 00)
    fechaDiaSiguiente = fecha + datetime.timedelta(1)
    fechaTexto = fechaDiaSiguiente.strftime('%Y%m%d')

    # Referencia para los productos de acumulación de radar en 24 horas
    referencias = {'Barcelona': 'r7ba0000.gif',
                   'Zaragoza': 'r7za0000.gif',
                   'Valencia': 'r7va0000.gif',
                   'Murcia': 'r7mu0000.gif'}

    outputPath = os.path.join(config.wwwPath,
                              'archivo',
                              fecha.strftime('%Y%m%d'))

    for radar in referencias.keys():
        fileName = 'acumulacion24Radar{radar}.gif'.format(radar=radar)
        filePath = os.path.join(outputPath, fileName)
        bigdata.bdpRequest( fechaTexto, referencias[radar], filePath)


def descargarImagenes(fecha):
    descargarImagenesVIM(fecha)
    descargarImagenesBigData(fecha)
