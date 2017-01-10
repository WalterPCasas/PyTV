import urllib
import cStringIO 
import Image

# Recupera un mapa de Static Google Maps server
def get_static_google_map(filename_wo_extension, center=None, zoom=None, imgsize="500x500", imgformat="jpeg",
                          maptype="roadmap", markers=None ):  
    
    # Ensambla la URL
    request =  "http://maps.google.com/maps/api/staticmap?" 
   
    # if center and zoom  are not given, the map will show all marker locations
    if center != None:
        request += "center=%s&" % center
        
    if center != None:
        request += "zoom=%i&" % zoom  # zoom 0 (all of the world scale ) to 22 (single buildings scale)


    request += "size=%ix%i&" % (imgsize) 
    request += "format=%s&" % imgformat
    request += "maptype=%s&" % maptype  # roadmap, satellite, hybrid, terrain


    # add markers 
    if markers != None:
        for marker in markers:
                request += "%s&" % marker

    request += "sensor=false&"   
    print request
    
    # Genera el archivo
    urllib.urlretrieve(request, filename_wo_extension+"."+imgformat) 


def newImage(latitud,longitud):
#if __name__ == '__main__':
    

    coordinates = str(latitud)+"%2C+"+str(longitud)

    marker_list = []
    marker_list.append("markers=size:mid|color:red|wight:7|"+coordinates)
   
    # make a map around a center
    get_static_google_map("../app/img/google_map_result", center=coordinates, zoom=9, imgsize=(530,630),
                          imgformat="png", maptype="roadmap", markers=marker_list)


print "Inicia carga de imagen...\nURL:\n"

newImage(latitud, longitud)

print "\nDone"