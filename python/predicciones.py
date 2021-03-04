import datetime
import http.client
import json
import requests
import socket

import key

def descargarPrediccion(valido, alcance, ccaa):
    alcance_texto = ['hoy','manana','pasadomanana','medioplazo'][alcance]
    fecha = (valido - datetime.timedelta(alcance)).strftime('%Y-%m-%d')
    
    try:
    
        # Hay un problema con el cifrado. Ubuntu 20.04 exige un nivel de
        # seguridad que no proporciona al servidor de opendata
        # Se rebaja el nivel de seguridad a 1
        hostname = socket.gethostname()
        # print('host', hostname)
        if hostname == 'gradullon':
            requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

        url = ('https://opendata.aemet.es/opendata/api/prediccion/ccaa/{alcance_texto}/{ccaa}' + '/elaboracion/{fecha}').format(**locals())
        queryString = {'api_key': key.OPENDATA_API_KEY}
        headers = {'cache-control': "no-cache"}
        res = requests.request("GET",url,headers=headers,params=queryString)

        url_datos = json.loads(res.text)['datos']
        res = requests.request("GET", url_datos, headers=headers)
    
        return res.text
    
    except:
        return 'No se ha podido descargar la predicción'

if __name__ == '__main__':
    fecha = datetime.date(2021,2,14)
    res = descargarPrediccion(fecha, 1, 'cat')
    print(res)
