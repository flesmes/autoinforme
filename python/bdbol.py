import collections
import ftplib
import sys

def fichero_peticion(nombres, boletin, emisor, desde, hasta):

    def quoted(st):
        return r'"' + st + r'"'

    bbdd = 'BDBOL'
    lifetime = 15 #minutos
    rango_fechas = '{d},{h}'.format(d=desde, h=hasta)

    Campo = collections.namedtuple('Campo', 'nombre valor')
    campos = [Campo('NFES',        quoted(nombres['estado'])),
              Campo('CUESTION',    ''),
              Campo('NFIC',        quoted(nombres['datos'])),
              Campo('LFTM',        lifetime),
              Campo('BBDD',        quoted(bbdd)),
              Campo('BDBOLETIN',   quoted(boletin)),
              Campo('BDBOLRFECHA', rango_fechas),
              Campo('BDBOLEMISOR', emisor)]
    
    with open(nombres['peticion'],'w') as file:
        for campo in campos:
            file.write('#{c.nombre} {c.valor}\n'.format(c = campo))

def request(boletin, emisor, fecha_inicio, fecha_fin):

    def solo_digitos(st):
        return ''.join(c for c in st if c.isdigit())

    def write_line(line):
        bol_bytes.extend(bytearray(line + '\n', 'utf8'))

    fecha_inicio = solo_digitos(fecha_inicio)
    fecha_fin = solo_digitos(fecha_fin)
    subfix = '{boletin}_{emisor}_{fecha_inicio}_{fecha_fin}'.format(**locals())
    nombres = {}
    nombres['peticion'] = 'peticion_' + subfix
    nombres['datos']    = 'datos_'    + subfix
    nombres['estado']   = 'estado_'   + subfix

    host = 'glaciar.aemet.es'
    port = 766
    user = 'gpvbn'
    passwd = '900Gpvbl'
    connection = ftplib.FTP()
    connection.connect(host,port)
    connection.login(user,passwd)

    fichero_peticion(nombres, boletin, emisor, fecha_inicio, fecha_fin)
    
    connection.cwd('peticiones')
    with open(nombres['peticion'], 'rb') as fichero_peticion_local:
        connection.storlines('STOR ' + nombres['peticion'],
                             fichero_peticion_local)

    connection.cwd('../datos')
    bol_bytes = bytearray()
    with open(nombres['datos'], 'w') as fichero_datos_local:
        connection.retrlines('RETR ' + nombres['datos'], write_line)
    
    connection.close()

    return bol_bytes.decode()

if __name__ == '__main__':
    if len(sys.argv) == 4:
        boletin = sys.argv[1]
        emisor = sys.argv[2]
        fecha = sys.argv[3]
        res = request(boletin, emisor, fecha, fecha)
        print(res)
    else:
        print('Uso: python3 bdbol.py boletin emisor fecha')
