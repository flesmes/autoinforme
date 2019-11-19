# -*- coding: utf-8 -*-

import datetime
import http.client
import json
import requests

def descargarPrediccion(valido, alcance, ccaa):
    alcance_texto = ['hoy','manana','pasadomanana','medioplazo'][alcance]
    fecha = (valido - datetime.timedelta(alcance)).strftime('%Y-%m-%d')
    
    url_opendata = 'opendata.aemet.es'
    conn = http.client.HTTPSConnection(url_opendata)
    headers = {'cache-control': "no-cache"}

    api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmbGVzbWVzekBhZW1ldC5lcyIsImp0aSI6IjRkNGI4MzdjLWJiMTQtNDEwZC1iYzBkLTQ3OTU0MDg3ZGRlNCIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTcyMjU1NjQ1LCJ1c2VySWQiOiI0ZDRiODM3Yy1iYjE0LTQxMGQtYmMwZC00Nzk1NDA4N2RkZTQiLCJyb2xlIjoiIn0.bNjsN7xAb14oWcur0QmQx8Z6xw9FVdxOGgGVfkZAdGE'

    url_peticion = ('/opendata/api/prediccion/ccaa/{alcance_texto}/{ccaa}' +
                    '/elaboracion/{fecha}/?api_key={api_key}'
                   ).format(**locals())

    try:
        conn.request("GET", url_peticion, headers=headers)
        res = conn.getresponse().read().decode()

        url_datos = json.loads(res)['datos']
        url_datos = url_datos.replace(url_opendata,'')
        conn.request("GET", url_datos, headers=headers)
        resp = conn.getresponse().read().decode('latin1').replace('\r','')

        return resp
    except:
        return 'No se ha podido descargar la predicción'

if __name__ == '__main__':
    fecha = datetime.date(2019,11,19)
    res = descargarPrediccion(fecha, 1, 'cat')
    print(res)
