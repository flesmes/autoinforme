# -*- coding: utf-8 -*-

import datetime
import re
import requests

ttaaiis = {1: 'FPSP75', 2: 'FPSP85'}
areas = {'cat': 'LEBN',
         'ara': 'LEZM',
         'val': 'LEVA',
         'bal': 'LEPM'}

def descargarBoletin(fecha, ttaaii, hora, minuto, area):
    # Obtener boletín mediante petición a la base de datos
    url = 'http://fujita.inm.es/bdbolpbolpet.php?fecha={}&tipo=FPSP&ttaaii={}&hora={}&minuto={}&emisor={}'.format(fecha,ttaaii,hora,minuto,area)
    response = requests.get(url).content.decode('latin-1')

    # Extraer el boletín. Se encuentra entre las cadenas ZCZC y NNNN
    return re.search('(?s)ZCZC(.*?)NNNN',response).group(1)

def descargarPrediccion(valido,alc,ar):
    fecha = (valido - datetime.timedelta(alc)).strftime('%d%m%Y')
    ttaaii = ttaaiis[alc]
    area = areas[ar]

    return descargarBoletin( fecha, ttaaii, '06', '00', area)

def descargarGuia(valido):
    fecha = valido.strftime('%d%m%Y')
    ttaaii = 'FPSP90'
    area = 'LEMM'

    return descargarBoletin( fecha, ttaaii, '00', '00', area)



