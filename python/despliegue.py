import jinja2
import os, os.path
import shutil
import socket

# config.py
def generateConfig():

    paths = { 'srcPath': srcPath, 'wwwPath': wwwPath}

    pathTemplates = os.path.join(paths['srcPath'], 'templates')

    jinjaEnv = jinja2.Environment(
        loader = jinja2.FileSystemLoader(pathTemplates),
        trim_blocks = True,
        lstrip_blocks = True)

    output = jinjaEnv.get_template('config.py').render(paths)
    destino = os.path.join(paths['srcPath'], 'python', 'config.py')
    with open(destino, 'w') as file:
        file.write(output)

    print('Creado config.py en ' + destino)

# Crear carpetas si no existen    
def crearCarpetas():
    
    dirs = ['archivo', 'css', 'js']
    paths = [os.path.join( wwwPath, dir) for dir in dirs]
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)

    path = os.path.join( srcPath, 'temp')
    if not os.path.exists(path):
        os.mkdir(path)
    

def copyFile( file, fuenteDir, destinoDir):
    fuente = os.path.join(fuenteDir, file)
    destino = os.path.join(destinoDir, file)
    shutil.copyfile(fuente, destino)

def saltar(file):
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
            if not saltar(file):
                copyFile( file, dirSrcPath, dirWwwPath)
    

hostname = socket.gethostname()
print('host', hostname)

if hostname == 'gradullon':
    srcPath = '/home/flesmes/Dropbox/Programacion/autoinforme/src'
    wwwPath = '/home/flesmes/Dropbox/Programacion/autoinforme/www'
else:
    srcPath = '/home/felipe/autoinforme'
    wwwPath = '/var/www/html'

generateConfig()

crearCarpetas()

copiarWwwSrc()

