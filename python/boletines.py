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
    
    remoto = 'http://fujita.inm.es/bdbolpbolpet.php?fecha={}&tipo=FPSP&ttaaii={}&hora=06&minuto=99&emisor={}'.format(fecha,alcance,area)
    response = requests.get(remoto).content.decode('latin-1')
    return re.search('(?s)ZCZC(.*?)NNNN',response).group(1)
    

