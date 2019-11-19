import datetime

# Lista de imagenes a descargar.
# Se incluye:
# remotefile - url de la imagen
# localfile  - nombre del archivo local
# width      - anchura de la imagen redimensionada

class Imgdata:

    def __init__(self,remoto,local,width):
        self.remotefile = remoto
        self.localfile = local
        self.width = width

def listaImagenes(fecha):
    images = []

    anterior = fecha - datetime.timedelta(1)
    siguiente = fecha + datetime.timedelta(1)
    dmas2 = fecha + datetime.timedelta(2)
    
    # *****************
    # Situación sinóptica
    # *****************

    #Imagen 1: Guia técnica de diagnóstico. Niveles Medios/Altos. Día D a las 12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/GT2/S1/000/GTDnaSAT.1.gif'.format(fecha.strftime('%Y%m%d')),
        'g22fa200_2.gif',
        640))

    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/GT2/S1/000/GTDna.1.gif'.format(fecha.strftime('%Y%m%d')),
        'GTDna.gif',
        640))

    #Imagen 2: Análisis de superficie. Día D a las 12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/GT2/S1/000/GTDnbSAT.1.gif'.format(fecha.strftime('%Y%m%d')),
        'gpx0a200_2.gif',
        640))

    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/GT2/S1/000/GTDnb.1.gif'.format(fecha.strftime('%Y%m%d')),
        'GTDnb.gif',
        640))

     #Imagen 3: P, Nubes Superficie. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/NUB.1.png'.format(fecha.strftime('%Y%m%d')),
        'MOD00CES1012NUB.1.png',
        640))

    #Imagen 4: T,Z Nivel 850. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/TZ_850.1.png'.format(fecha.strftime('%Y%m%d')),
        'MOD00CES1012TZ_850.1.png',
        640))

    #Imagen 5: T,Z Nivel 500. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/TZ_500.1.png'.format(fecha.strftime('%Y%m%d')),
        'MOD00CES1012TZ_500.1.png',
        640))

    #Imagen 6: T,Z Nivel 300. Pasada del día D a las 00. Alcance +12
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CE/S1/012/TZ_300.1.png'.format(fecha.strftime('%Y%m%d')),
        'MOD00CES1012TZ_300.1.png',
        640))

    # *****************
    # Precipitación
    # *****************

    #Imagen 1.1: Precipitación 24 H observada SEMAS
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Prec_{}_0000_24.jpg'.format(siguiente.strftime('%d%m%Y')),
        'P_Prec__0000_24_2.jpg',
        640))

    #Imagen 1.2: Precipitación 24 H observada SAIH Ebro
    images.append( Imgdata(
        'http://www.saihebro.com/saihebro/img/pluviometrias/evolucion//PACUM_{}-00.PNG'.format(siguiente.strftime('%Y-%m-%d')),
        'Pcp24_SAIHEbro.jpg',
        640))

    #Imagenes 2,3,4: Precipitación 24 H. Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00, D-1 12, D 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/PCP_24.1.png'.format(anterior.strftime('%Y%m%d'),mod),
            'MOD00{}P1048PCP_24.1.png'.format(mod),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/{}/P1/036/PCP_24.1.png'.format(anterior.strftime('%Y%m%d'),mod),
            'MOD12{}P1036PCP_24.1.png'.format(mod),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/024/PCP_24.1.png'.format(fecha.strftime('%Y%m%d'),mod),
            'MOD00{}P1024PCP_24.1.png'.format(mod),
            640))

    for umbral in ['1', '5', '20', '40']:
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CEEPSP1/P1/048/PDP_24_{}.1.png'.format(anterior.strftime('%Y%m%d'),umbral),
            'MOD00CEEPSP1P1048PDP_24_{}.1.png'.format(umbral),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/12/CEEPSP1/P1/036/PDP_24_{}.1.png'.format(anterior.strftime('%Y%m%d'),umbral),
            'MOD12CEEPSP1P1036PDP_24_{}.1.png'.format(umbral),
            640))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/CEEPSP1/P1/024/PDP_24_{}.1.png'.format(fecha.strftime('%Y%m%d'),umbral),
            'MOD00CEEPSP1P1024PDP_24_{}.1.png'.format(umbral),
            640))
        


    # *****************
    # Nieve
    # *****************

    #Imagen 1: Nieve 24 H estimada 
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Nieve_{}_0000_24.jpg'.format(siguiente.strftime('%d%m%Y')),
        'P_Nieve__0000_24_2.jpg',
        640))

    #Imagenes 2,3,4: Nieve 24 H. Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/NIEVE_24.1.png'.format(anterior.strftime('%Y%m%d'),mod),
            'MOD00{}P1048NIEVE_24.1.png'.format(mod),
            640))

    #Imagenes 5,6: Cota de nieve mínima en 24 H. Modelo IFS, HARM 40
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/COTANIEMIN_24.1.png'.format(anterior.strftime('%Y%m%d'),mod),
            'MOD00{}P1048COTANIEMIN_24.1.png'.format(mod),
            640))

    # *****************
    # Viento Racha máxima en 24 horas
    # *****************

    #Imagen 1: Observada
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Racha_{}_0000_24.jpg'.format(siguiente.strftime('%d%m%Y')),
        'P_Racha_0000_24.jpg',
        640))

    #Imagenes 2,3,4: Modelo IFS, HARM 40, HARM 38
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR', 'HMAR2']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/RACHAMAX_24.1.png'.format(anterior.strftime('%Y%m%d'),mod),
            'MOD00{}P1048RACHAMAX_24.1.png'.format(mod),
            640))

    # *****************
    # Temperatura máxima
    # *****************

    #Imagen 1: Observada
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Max_{}_0000_24.jpg'.format(siguiente.strftime('%d%m%Y')),
        'P_Max_0000_24.jpg',
        640))

    #Imagen 2: Postproceso
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/postproceso/nuevasTemperaturas/mapas/00/P/ma_1.png'.format(anterior.strftime('%Y%m%d')),
        'postproceso00tmax.png',
        640))

    #Imagenes 3,4: Modelo IFS, HARM 40
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/TMAX_24.1.png'.format(anterior.strftime('%Y%m%d'),mod),
            'MOD00{}P1048TMAX_24.1.png'.format(mod),
            640))

    # *****************
    # Temperatura mínima
    # *****************

    #Imagen 1: Observada
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Min_{}_0000_24.jpg'.format(siguiente.strftime('%d%m%Y')),
        'P_Min_0000_24.jpg',
        640))

    #Imagen 2: Postproceso
    images.append( Imgdata(
        'http://sureste.aemet.es/stapwww/archivotemporal/{}/postproceso/nuevasTemperaturas/mapas/00/P/mi_1.png'.format(anterior.strftime('%Y%m%d')),
        'postproceso00tmin.png',
        640))

    #Imagenes 3,4: Modelo IFS, HARM 40
    # Pasadas D-1 00
    for mod in ['CE', 'HMAR']: 
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/MOD/00/{}/P1/048/TMIN_24.1.png'.format(anterior.strftime('%Y%m%d'),mod),
            'MOD00{}P1048TMIN_24.1.png'.format(mod),
            640))

    # *****************
    # EFI
    # *****************

    #Imagen 1: PCP 
    images.append( Imgdata(
        'http://sureste.inm.es/stapwww/archivotemporal/{}/MOD/00/CEEPSE/P1/024/EFIPCP_24.1.png'.format(fecha.strftime('%Y%m%d')),
        'CEEPSEP1_EFIPCP_241_2.png',
        640))

    #Imagen 2: Nieve 
    images.append( Imgdata(
        'http://sureste.inm.es/stapwww/archivotemporal/{}/MOD/00/CEEPSE/P1/024/EFINIE.1.png'.format(fecha.strftime('%Y%m%d')),
        'CEEPSEP1_EFINIE1_2.png',
        640))

    #Imagen 3: TMAX 
    images.append( Imgdata(
        'http://sureste.inm.es/stapwww/archivotemporal/{}/MOD/00/CEEPSE/P1/024/EFITMAX.1.png'.format(fecha.strftime('%Y%m%d')),
        'CEEPSEP1_EFITMAX1_2.png',
        640))

    #Imagen 4: TMIN
    images.append( Imgdata(
        'http://sureste.inm.es/stapwww/archivotemporal/{}/MOD/00/CEEPSE/P1/024/EFITMIN.1.png'.format(fecha.strftime('%Y%m%d')),
        'CEEPSEP1_EFITMIN1_2.png',
        640))

    #Imagen 5: Rachas
    images.append( Imgdata(
        'http://sureste.inm.es/stapwww/archivotemporal/{}/MOD/00/CEEPSE/P1/024/EFIRACH.1.png'.format(fecha.strftime('%Y%m%d')),
        'CEEPSEP1_EFIRACH1_2.png',
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
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/RAD/{}/NAC/00_RA2D.PNG'.format(fecha.strftime('%Y%m%d'),hora),
            'RAD{}NAC00_RA2D.PNG'.format(hora),
            950))
        images.append( Imgdata(
            'http://sureste.aemet.es/stapwww/archivotemporal/{}/RAD/{}/NAC/00_ACC.PNG'.format(fecha.strftime('%Y%m%d'),hora),
            'RAD{}NAC00_ACC.PNG'.format(hora),
            950))

    # *****************
    # Nubes bajas
    # *****************
 
    # IR10.8 y clases CT


#    for h in range(24):
#        if h < 10:
#            hora = '0' + str(h)
#        else:
#            hora = str(h)
#        images.append( Imgdata(
#            'http://sureste.aemet.es/stapwww/archivotemporal/{}/SAT/{}/NWCSAF_MN/P1/00_CT_Bajas.PNG'.format(fecha.strftime('%Y%m%d'),hora),
#            'SAT{}NWCSAF_MNP100_CT_Bajas.PNG'.format(hora),
#            810))

    # *****************
    # Rayos
    # *****************

    #Imagen 1: Rayos 24 H observados 
    images.append( Imgdata(
        'http://www0.inm.es/wwx/webpagin/MapasAutomaticos/mapas/P_Rayos_{}_0000_24.jpg'.format(siguiente.strftime('%d%m%Y')),
        'P_Rayos__0000_24_2.jpg',
        640))

    #Imagen 2: Rayos 24 H observados 
    images.append( Imgdata(
        'http://sureste.inm.es/stapwww/archivotemporal/{}/RAD/00/NAC/00_RAY_24h.PNG'.format(siguiente.strftime('%Y%m%d')),
        'rayos_24h.png',
        480))

    # Harmonie. Densidad de rayos
    # D+1
    images.append( Imgdata(
        'http://noreste.aemet.es/pn33/ngiv-r/iberia/img0/s0-24.png',
        '{}/rayos_harmonie_d1.png'.format(siguiente.strftime('%Y%m%d')),
        696))

    # Harmonie. Densidad de rayos
    # D+2
    images.append( Imgdata(
        'http://noreste.aemet.es/pn33/ngiv-r/iberia/img0/s1-24.png',
        '{}/rayos_harmonie_d2.png'.format(dmas2.strftime('%Y%m%d')),
        696))


    return images

