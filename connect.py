# -*- coding: utf-8 -*-
import urllib2,unicodedata
from bs4 import BeautifulSoup


def generador(name, value):
    startTime = value[1]
    arcEstado = open('app/txt/txtStartTime.txt', 'w')
    arcEstado.write("Inicio: " + startTime)
    arcEstado.close()

    arcMessage = open('app/txt/txtMessage.txt', 'w')
    arcMessage.write("Alerta de Sismo")
    arcMessage.close()

    severe = value[7]
    arcSevere = open('app/txt/txtSevere.txt', 'w')
    arcSevere.write("Intensidad: " + severe)
    arcSevere.close()

    print "Done"

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
        #print td_list
    	name.append(td_list[0].string)
        #print(td_list[1].string)
    	value.append(td_list[1].string)
    generador(name, value)  

    #print(value[5])

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
