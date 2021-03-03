import datetime
import http.client
import json
import requests

def descargarPrediccion(valido, alcance, ccaa):
    alcance_texto = ['hoy','manana','pasadomanana','medioplazo'][alcance]
    fecha = (valido - datetime.timedelta(alcance)).strftime('%Y-%m-%d')
    
    api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmbGVzbWVzekBhZW1ldC5lcyIsImp0aSI6IjRkNGI4MzdjLWJiMTQtNDEwZC1iYzBkLTQ3OTU0MDg3ZGRlNCIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTcyMjU1NjQ1LCJ1c2VySWQiOiI0ZDRiODM3Yy1iYjE0LTQxMGQtYmMwZC00Nzk1NDA4N2RkZTQiLCJyb2xlIjoiIn0.bNjsN7xAb14oWcur0QmQx8Z6xw9FVdxOGgGVfkZAdGE'
    
    try:
    
        # Hay un problema con el cifrado. Ubuntu 20.04 exige un nivel de
        # seguridad que no proporciona al servidor de opendata
        # Se rebaja el nivel de seguridad a 1
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

        url = ('https://opendata.aemet.es/opendata/api/prediccion/ccaa/{alcance_texto}/{ccaa}' + '/elaboracion/{fecha}').format(**locals())
        queryString = {'api_key': api_key}
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
