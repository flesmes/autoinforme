# -*- coding: utf-8 -*-

import datetime
import re
import requests

alcances = {1: 'FPSP75', 2: 'FPSP85'}
areas = {'cat': 'LEBN',
         'ara': 'LEZM',
         'val': 'LEVA',
         'bal': 'LEPM'}

def descargarBoletin(valido,alc,ar):
    fecha = (valido - datetime.timedelta(alc)).strftime('%d%m%Y')
    alcance = alcances[alc]
    area = areas[ar]

    # Obtener boletín mediante petición a la base de datos
    url = 'http://fujita.inm.es/bdbolpbolpet.php?fecha={}&tipo=FPSP&ttaaii={}&hora=06&minuto=99&emisor={}'.format(fecha,alcance,area)
    response = requests.get(url).content.decode('latin-1')

    # Extraer el boletín. Se encuentra entre las cadenas ZCZC y NNNN
    return re.search('(?s)ZCZC(.*?)NNNN',response).group(1)
    

