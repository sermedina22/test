import math
#funciones para calcula distancias
def distancia(lat1,long1,lat2,long2):
    dlat=lat2-lat1
    dlong=long2-long1
    Rt=6372.795477598 #km
    dist=2*Rt*math.asin(math.sqrt(math.sin(dlat/2)**2+ (math.cos(lat1)*math.cos(lat2)*math.sin(dlong/2)**2)  ))
    return dist
    
def obtenermascercanos(lata,longa, zonasw):
    dlist=[]
    for i in range(len(zonasw)):
        [d,u] = [distancia(lata, longa,zonasw[i][0],zonasw[i][1]), zonasw[i][2]]#guardamos distancia, usuarios por cada zona wifi
        dlist.append([d,u]) #los agregamos a la lista
    print (*dlist)
    dlist=sorted(dlist, key=lambda x: x[1])  #la organizamos por usuarios de menor a mayor
    return dlist


def direccion(lat,long,latw,longw): 
    if lat!=latw or long!=longw:   
        dir="Para llegar a la zona wifi dirigirse primero "
        if long<longw:
             dir+="al oriente " 
        elif long>longw:
            dir+="a el occidente"
        if dir!="Para llegar a la zona wifi dirigirse primero " and lat!=latw:
            dir+=" luego "           
        if lat<latw:
             dir+="hacia el norte"
        elif lat>latw:
            dir+="hacia el sur"
    else: dir="Ya se encuentra en la ubicación"
    print(dir)
    
def tiempop(distance):
    [tb,tm]=[(distance/3.33)/60,(distance/19.44)/60]
    print("El tiempo promedio en bicicleta es {} minutos".format(round(tb)))  
    print("El tiempo promedio en motocicleta es {} minutos".format(round(tm)))  




Zonaswifi=[[2.698,-76.680,63],[2.724,-76.693,30],[2.606,-76.742,680],[2.698,-76.690,15]]
xx=obtenermascercanos(2.71,-76.71,Zonaswifi)
direccion(2.71,-76.71,2.698,-76.690)
tiempop(xx[0][0])


            
