# -*- coding: latin-1 -*-

import datetime

class Imgdata:

    def __init__(self,remoto,local,width):
        self.remotefile = remoto
        self.localfile = local
        self.width = width

def listaImagenes(fecha):
    images = []

    actual = fecha.strftime('%Y%m%d')
    anterior = (fecha - datetime.timedelta(1)).strftime('%Y%m%d')
    siguiente = (fecha + datetime.timedelta(1)).strftime('%d%m%Y')
    
    # *****************
    # Situación sinóptica
    # *****************

    #Imagen 1: Guia técnica de diagnóstico. Niveles Medios/Altos. Día D a las 12
    images.append( Imgdata(
        'http://turbonada.aemet.es/adjuntos/prod/GTDP/g22fa200.gif',
        'g22fa200.gif',
        640))

    #Imagen 2: Guia técnica de diagnóstico. Niveles Medios/Altos. Día D a las 12
    images.append( Imgdata(
        'http://turbonada.aemet.es/adjuntos/prod/GTDP/gpx0a200.gif',
        'gpx0a200.gif',
        640))

    #Imagen 3: P, Nubes Superficie. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/NUB.1.png'.format(actual),
        'MOD00CES1012NUB.1.png',
        640))

    #Imagen 4: T,Z Nivel 850. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/TZ_850.1.png'.format(actual),
        'MOD00CES1012TZ_850.1.png',
        640))

    #Imagen 5: T,Z Nivel 500. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/TZ_500.1.png'.format(actual),
        'MOD00CES1012TZ_500.1.png',
        640))

    #Imagen 6: T,Z Nivel 300. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/TZ_300.1.png'.format(actual),
        'MOD00CES1012TZ_300.1.png',
        640))

    # *****************
    # Precipitación
    # *****************

    #Imagen 1: Precipitación 24 H observada 
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Prec_{}_0000_24.jpg'.format(siguiente),
        'P_Prec_0000_24.jpg',
        640))

    #Imagenes 2,3,4: Precipitación 24 H. Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00, D-1 12, D 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/PCP_24.1.png'.format(anterior,mod),
            'MOD00{}P1048PCP_24.1.png'.format(mod),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/{}/P1/036/PCP_24.1.png'.format(anterior,mod),
            'MOD12{}P1036PCP_24.1.png'.format(mod),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/024/PCP_24.1.png'.format(actual,mod),
            'MOD00{}P1024PCP_24.1.png'.format(mod),
            640))

    for umbral in ['1', '5', '20', '40']:
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CEEPSP1/P1/048/PDP_24_{}.1.png'.format(anterior,umbral),
            'MOD00CEEPSP1P1048PDP_24_{}.1.png'.format(umbral),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/CEEPSP1/P1/036/PDP_24_{}.1.png'.format(anterior,umbral),
            'MOD12CEEPSP1P1036PDP_24_{}.1.png'.format(umbral),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CEEPSP1/P1/024/PDP_24_{}.1.png'.format(actual,umbral),
            'MOD00CEEPSP1P1024PDP_24_{}.1.png'.format(umbral),
            640))
        


    # *****************
    # Nieve
    # *****************

    #Imagen 1: Nieve 24 H estimada 
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Nieve_{}_0000_24.jpg'.format(siguiente),
        'P_Nieve_0000_24.jpg',
        640))

    #Imagenes 2,3,4: Nieve 24 H. Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/NIEVE_24.1.png'.format(anterior,mod),
            'MOD00{}P1048NIEVE_24.1.png'.format(mod),
            640))

    #Imagenes 5,6: Cota de nieve mínima en 24 H. Modelo IFS, HARM 40
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/COTANIEMIN_24.1.png'.format(anterior,mod),
            'MOD00{}P1048COTANIEMIN_24.1.png'.format(mod),
            640))

    # *****************
    # Viento Racha máxima en 24 horas
    # *****************

    #Imagen 1: Observada
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Racha_{}_0000_24.jpg'.format(siguiente),
        'P_Racha_0000_24.jpg',
        640))

    #Imagenes 2,3,4: Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/RACHAMAX_24.1.png'.format(anterior,mod),
            'MOD00{}P1048RACHAMAX_24.1.png'.format(mod),
            640))

    # *****************
    # Temperatura máxima
    # *****************

    #Imagen 1: Observada
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Max_{}_0000_24.jpg'.format(siguiente),
        'P_Max_0000_24.jpg',
        640))

    #Imagenes 2,3,4: Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/TMAX_24.1.png'.format(anterior,mod),
            'MOD00{}P1048TMAX_24.1.png'.format(mod),
            640))

    # *****************
    # Temperatura mínima
    # *****************

    #Imagen 1: Observada
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Min_{}_0000_24.jpg'.format(siguiente),
        'P_Min_0000_24.jpg',
        640))

    #Imagenes 2,3,4: Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/TMIN_24.1.png'.format(anterior,mod),
            'MOD00{}P1048TMIN_24.1.png'.format(mod),
            640))

    # *****************
    # Radar
    # *****************
 
    # Radar Nacional, Diagnóstico 2D, Imagenes cada hora

    for h in range(24):
        if h < 10:
            hora = '0' + str(h)
        else:
            hora = str(h)
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/RAD/{}/NAC/00_RA2D.PNG'.format(actual,hora),
            'RAD{}NAC00_RA2D.PNG'.format(hora),
            950))

    # *****************
    # Nubes bajas
    # *****************
 
    # IR10.8 y clases CT


    for h in range(24):
        if h < 10:
            hora = '0' + str(h)
        else:
            hora = str(h)
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/SAT/{}/NWCSAF_MN/P1/00_CT_Bajas.PNG'.format(actual,hora),
            'SAT{}NWCSAF_MNP100_CT_Bajas.PNG'.format(hora),
            810))

#    for image in images:
#        print(image.remotefile)
                
    return images

