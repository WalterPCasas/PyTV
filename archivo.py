# -*- coding: utf-8 -*-
import urllib2,unicodedata
from bs4 import BeautifulSoup
 
#método de análisis de una dirección web
def analisisDescarga(conexion):
    html = conexion.read()
    print("Hasta aqui llega1")
    soup = BeautifulSoup(html)
    print("Hasta aqui llega2")
    #obtenemos una lista de String con la condición de atributos class con valores details y price
    links = soup.find_all(True, {'class':['details','price']})
    #la lista alterna valores de nombre de producto y precio
    #   creamos una bandera para diferenciar si es valor o producto
    print("Hasta aqui llega3")
    precio = False
    for tag in links:
        print("--")
        for linea in tag:
            linea = linea.strip();
            #adaptamos unicode a utf-8
            normalizado=unicodedata.normalize('NFKD', linea).encode('ascii','ignore')
 
            if len(normalizado)>1:
                if precio:
                    print('precio: '+normalizado)
                    precio= not precio
                    archivo.write(normalizado+'\n')
                else:
                    print('producto: '+normalizado)
                    precio = not precio
                    archivo.write(normalizado+'\t')
#este método se conectará con la web y establece un timeout que obliga a reintentar el fallo
def preparar(web):
    try:
        print(web)
        conector = urllib2.urlopen(web,timeout=10)#timeout de 10 segundos
        analisisDescarga(conector)
    except:
        print("Tiempo de espera agotado, volviendo a intentar")
        preparar(web)
 
#Programa principal
print('Comienza el programa')

#Ruta de la página web
url = 'http://ultimosismo.igp.gob.pe/'
preparar(url)
 
archivo.close()
print('Fin del programa')