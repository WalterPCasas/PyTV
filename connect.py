# -*- coding: utf-8 -*-
import urllib2,unicodedata
from bs4 import BeautifulSoup


def generador(name, value):
	print(name)
	print(value)

# Extraemos el HTML y ubicamos lo que queremos
def analisisDescarga(conexion):
    html = conexion.read()
    soup = BeautifulSoup(html, "html.parser")
    name = list()
    value = list()
    #obtenemos una lista de String con la condición de atributos class "cebra"
    tabla = soup.find_all(True, {'class':['cebra']})
    for tag in tabla:
    	td_list = tag.find_all("td");
    	name.append(td_list[0].string)
    	value.append(td_list[1].string)
    generador(name, value)  

# Revisa la conexión de la página e intenta hasta que conecte
def preparar(web):
    try:
        print(web)
        conector = urllib2.urlopen(web,timeout=15)#timeout de 10 segundos
        analisisDescarga(conector)
    except:
        print("Tiempo de espera agotado, volviendo a intentar")
        preparar(web)
 
#Programa principal
print('Comienza el programa')

#Ruta de la página web
url = 'http://ultimosismo.igp.gob.pe/'
preparar(url)
