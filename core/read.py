# -*- coding: utf-8 -*-
### lector.py : lectura de archivo XML
### para hacer uso de la librería las etiquetas deben abrir y cerrar

from lxml import etree
docx = etree.parse('../input/ejemplo.xml')

raiz = docx.getroot()

# print raiz.tag
# print len(raiz)
### tener cuidado con los indices del arreglo, lee comentarios XML como etiqueta

estado = raiz[2].text
tipoMensaje = raiz[3].text
informacion = raiz[6]

evento = informacion[2].text
tipoRespuesta = informacion[3].text
severidad = informacion[5].text
inicio = informacion[8].text
fin = informacion[9].text
parametros = informacion[11].text
area = informacion[12].text

print estado +"\t|"+ tipoMensaje +"\t|"+ evento
print tipoRespuesta +"\t|"+ severidad
print inicio +"\t|"+ fin
print parametros 
print area

### Creating Title
tipoRespuesta = tipoRespuesta.upper()

arcEstado = open('../app/txt/txtTitle.txt', 'w')
arcEstado.write("      ¡"+tipoRespuesta+"!")
arcEstado.close()

### Creating Parameters
arcParameters = open('../app/txt/txtParameters.txt', 'w')
arcParameters.write(parametros)
arcParameters.close() 

### Creating Message
tipoMensaje = tipoMensaje.capitalize()
arcMessage = open('../app/txt/txtMessage.txt', 'w')
arcMessage.write(tipoMensaje + " " + evento)
arcMessage.close()

### Creating Severe
severidad = severidad.capitalize()
arcSevere = open('../app/txt/txtSevere.txt', 'w')
arcSevere.write("Intensidad: "+severidad)
arcSevere.close()

### Creating Start Time
tuplaStart = inicio.partition("T")
# print tuplaStart
tS1, tS2,tS3 = tuplaStart
tS3div = tS3.partition("-")
tS3div1, tS3div2, tS3div3 = tS3div
# print tS3div
arcStartTime = open('../app/txt/txtStartTime.txt', 'w')
arcStartTime.write("Inicio: "+tS3div3+" - "+tS1)
arcStartTime.close()

### Creating End Time
tuplaStart = fin.partition("T")
# print tuplaStart
tS1, tS2,tS3 = tuplaStart
tS3div = tS3.partition("-")
tS3div1, tS3div2, tS3div3 = tS3div
# print tS3div
arcStartTime = open('../app/txt/txtEndTime.txt', 'w')
arcStartTime.write("Fin: "+tS3div3+" - "+tS1)
arcStartTime.close()

print "Listo"
