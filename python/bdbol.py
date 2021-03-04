from collections import namedtuple
import ftplib
import io
import os
import sys
import time

import config
import key

def formularioPeticion(nombres, boletin, emisor, desde, hasta):

    def quoted(st):
        return r'"' + st + r'"'

    bbdd = 'BDBOL'
    lifetime = 15 #minutos
    rango_fechas = '{d},{h}'.format(d=desde, h=hasta)
    path_peticion = os.path.join( config.srcPath,
                                  'temp',
                                  nombres['peticion'])

    Campo = namedtuple('Campo', 'nombre valor')
    campos = [Campo('NFES',        quoted(nombres['estado'])),
              Campo('CUESTION',    ''),
              Campo('NFIC',        quoted(nombres['datos'])),
              Campo('LFTM',        lifetime),
              Campo('BBDD',        quoted(bbdd)),
              Campo('BDBOLETIN',   quoted(boletin)),
              Campo('BDBOLRFECHA', rango_fechas),
              Campo('BDBOLEMISOR', emisor)]
    
    lines = ['#{c.nombre} {c.valor}'.format(c = campo) for campo in campos]
    return '\n'.join(lines)

def request(boletin, emisor, fecha_inicio, fecha_fin):

    def solo_digitos(st):
        return ''.join(c for c in st if c.isdigit())

    fecha_inicio = solo_digitos(fecha_inicio)
    fecha_fin = solo_digitos(fecha_fin)
    fmt = '{boletin}_{emisor}_{fecha_inicio}_{fecha_fin}'
    subfix = fmt.format(**locals())
    nombres = {}
    nombres['peticion'] = 'peticion_' + subfix
    nombres['datos']    = 'datos_'    + subfix
    nombres['estado']   = 'estado_'   + subfix
    path_peticion_local = os.path.join( config.srcPath,
                                        'temp',
                                        nombres['peticion'])
    host = 'glaciar.aemet.es'
    port = 766
    user = 'gpvbn'
    passwd = key.BDBOL_KEY
    connection = ftplib.FTP()
    connection.connect(host,port)
    connection.login(user,passwd)

    peticion = formularioPeticion(nombres,
                                   boletin,
                                   emisor,
                                   fecha_inicio,
                                   fecha_fin)
    streamPeticion = io.BytesIO( bytes(peticion,'utf8'))
    
    connection.cwd('peticiones')
    connection.storlines('STOR ' + nombres['peticion'], streamPeticion)
    streamPeticion.close()

    time.sleep(2)

    connection.cwd('../datos')
    bol_lines = []
    connection.retrlines('RETR ' + nombres['datos'], bol_lines.append)
    
    connection.close()

    body = slice(5,-5)
    return '\n'.join(bol_lines)[body]

if __name__ == '__main__':
    if len(sys.argv) == 4:
        boletin = sys.argv[1]
        emisor = sys.argv[2]
        fecha = sys.argv[3]
        res = request(boletin, emisor, fecha, fecha)
        print(res)
    else:
        print('Uso: python3 bdbol.py boletin emisor fecha')
