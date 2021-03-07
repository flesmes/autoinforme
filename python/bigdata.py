import datetime
import json
import os.path
import requests
import shutil

import config
import key

class RequestError(Exception):
    pass

def bigdataRequest(url, outputFile):

    noDisponiblePath = os.path.join( config.srcPath,
                                     'templates',
                                     'nodisponible.gif')
    
    querystring = {'api_key':key.BIGDATA_API_KEY}
    headers = {'cache-control': 'no-cache'}


    try:
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
            raise RequestError

    except Exception:
            
        print('No se han podido obtener los datos para url {url}. Codigo de estado:{estado}'.format(url=url,estado=estado))
        shutil.copyfile( noDisponiblePath, outputFile)
        

def bdpRequest(fecha, refProducto, outputFile):

    #Url de la llamada al rest
    url = 'http://bigdata.aemet.es/bigdatarest/api/bdp/binario/fecha/{fecha}/refproducto/{ref}'.format(fecha=fecha, ref=refProducto)

    bigdataRequest(url, outputFile)

