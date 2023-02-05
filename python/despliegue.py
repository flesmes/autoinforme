import os, os.path
import shutil
import socket

# config.py
def generateConfigScript():
    destino = os.path.join(srcPath, 'python', 'config.py')
    with open(destino, 'w') as file:
        file.write("srcPath = '{path}'\n".format(path=srcPath))
        file.write("\n")
        file.write("wwwPath = '{path}'\n".format(path=wwwPath))

    print('Creado config.py en ' + destino)
 
# Crear carpetas si no existen    
def crearCarpetas():

    # Carpetas en wwwPath
    dirs = ['archivo', 'css', 'js']
    for dir in dirs:
        path = os.path.join(wwwPath, dir)
        if not os.path.exists(path):
            os.mkdir(path)
            
def copyFile( file, fuenteDir, destinoDir):
    fuente = os.path.join(fuenteDir, file)
    destino = os.path.join(destinoDir, file)
    shutil.copyfile(fuente, destino)

def ignorable(file):
    return file[-1] == '~'

def copiarWwwSrc():

    copyFile( 'index.html',
              os.path.join( srcPath, 'html'),
              wwwPath)

    for dir in ['css', 'js']:
        dirSrcPath = os.path.join(srcPath, dir)
        dirWwwPath = os.path.join(wwwPath, dir)
        files = os.listdir(dirSrcPath)
        for file in files:
            if not ignorable(file):
                copyFile( file, dirSrcPath, dirWwwPath)
    

hostname = socket.gethostname()
print('host', hostname)

if hostname == 'pamplona-ubuntu':
    srcPath = '/home/felipe/Programacion/autoinforme/src'
    wwwPath = '/home/felipe/Programacion/autoinforme/www'
else:
    srcPath = '/home/felipe/autoinforme'
    wwwPath = '/var/www/html'

generateConfigScript()

crearCarpetas()

copiarWwwSrc()
