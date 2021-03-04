import datetime
import json
import os.path
import requests
import shutil

import config
import key

def bigdataRequest(url, outputFile):

    noDisponiblePath = os.path.join( config.path_base,
                                     'templates',
                                     'nodisponible.gif')
    
    querystring = {'api_key':key.BIGDATA_API_KEY}
    headers = {'cache-control': 'no-cache'}


    #Hacemos la llamada
    response = requests.request('GET',
                                url,
                                headers=headers,
                                params=querystring,
                                verify=False)

    #Obtenemos el json de la respuesta
    data = json.loads(response.text)

    estado = data['estado']

    #Si el estado es 200 (exito) obtenemos los datos
    # y los guardamos en un fichero
    if (estado == 200):
        print('Descargado con éxito {url}'.format(url=url))
        
        urlDatos = data['datos']
        datos = requests.request('GET',
                                 urlDatos,
                                 headers=headers,
                                 params=querystring,
                                 verify=False)

        #Insertamos los datos en un fichero
        fich_datos = open(outputFile,'wb')
        fich_datos.write(datos.content)
        fich_datos.close()
    else:
        print('No se han podido obtener los datos para url {url}. Codigo de estado:{estado}'.format(url=url,estado=estado))
        shutil.copyfile( noDisponiblePath, outputFile)
        

def bdpRequestFecha( fecha, refProducto, outputFile):

    #Url de la llamada al rest
    url = 'http://bigdata.aemet.es/bigdatarest/api/bdp/binario/fecha/{fecha}/refproducto/{ref}'.format(fecha=fecha, ref=refProducto)

    bigdataRequest(url, outputFile)

# Descarga de imágenes de estimación por radar de acumulación de precipitación en 24 horas
def descargarFromBigData(fecha, outputPath):

    # La fecha para la URL es la del día siguiente (a las 00)
    fechaDiaSiguiente = fecha + datetime.timedelta(1)
    fechaTexto = fechaDiaSiguiente.strftime('%Y%m%d')

    # Referencia para los productos de acumulación de radar en 24 horas
    referencias = {'Barcelona': 'r7ba0000.gif',
                   'Zaragoza': 'r7za0000.gif',
                   'Valencia': 'r7va0000.gif',
                   'Murcia': 'r7mu0000.gif'}

    for radar in referencias.keys():
        fileName = 'acumulacion24Radar{radar}.gif'.format(radar=radar)
        filePath = os.path.join(outputPath, fileName)
        bdpRequestFecha( fechaTexto, referencias[radar], filePath)

if __name__ == '__main__':
    #Parametros de la busqueda
    fecha = datetime.date(2021, 3, 1)
    descargarFromBigData(fecha, config.pathArchivo)
