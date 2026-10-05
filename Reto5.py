import math
import pandas as pd
#funciones utilizadas
def creaM(n,m):
    matriz = []
    for i in range(n):
        a = [0.000]*m
        matriz.append(a)
    return matriz

def dibuja3M(M):#mostrador de matriz
    name=['Casa   ','Trabajo','Parque ']
    print("Coordenadas Actuales")
    for i in range(len(M)):
        print (str(name[i]) +' '+  str(M[i]))


def promedioM(M):#promedios matriz
    plat=0
    plong=0
    for i in range(len(M)):
        for j in range(len(M[i])): 
            M[i][j]=round(M[i][j] ,3) #aprovechamos para redondear a 3 digitos           
            if j==0:
                plat=plat+M[i][j] 
            if j==1:
                plong=plong+M[i][j]    
    plat=round((plat/len(M)),3 )   
    plong=round((plong/len(M)),3 )      
    p=[plat, plong]
    return p

def masalsur(M):
    for i in range(len(M)):
        for j in range(len(M[i])): 
            if i==0 and j==0:
                menor=M[i][j]
            if j==0 and M[i][j] <= menor:
                menor=M[i][j] 
    return round(menor,3)
          
    

#  Inf:2.548 Sup: 2.766"
def vallat(coordenada):
    if (float(coordenada)>=2.548 and float(coordenada)<=2.766):
        return float(coordenada)
# longitud Occ:-76.879  Or:-76.493
def vallong(coordenada):
    if (float(coordenada)>=-76.879 and float(coordenada)<=-76.493):
        return float(coordenada)

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
        [d,u,latw,longw] = [distancia(lata, longa,zonasw[i][0],zonasw[i][1]), zonasw[i][2],zonasw[i][0],zonasw[i][1]]#guardamos distancia, usuarios por cada zona wifi
        dlist.append([d,u,latw,longw]) #los agregamos a la lista
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
    print("El tiempo promedio en bicicleta es {} minutos".format(round(tb,2)))  
    print("El tiempo promedio en motocicleta es {} minutos".format(round(tm,2)))  

ubiok=False
Zonaswifi=[[2.698,-76.680,63],[2.724,-76.693,30],[2.606,-76.742,680],[2.698,-76.690,15]]
zw=pd.DataFrame(Zonaswifi,columns=['Latitud','Longitud','Personas'])
zw.to_csv('Zwifi.csv',index=False )# creamos el archivo por si no esta para poder leerlo

#  msg bienvenida
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario='51743'
contraseña=usuario[::-1] #usuario alreves
egg='m1s10nt1c'
inus=input("Nombre de usuario:")
inpass=input("Contraseña:")
if (usuario==inus) and (contraseña==inpass or egg==inpass):  

    t1=usuario[2:5] # ultimos 3 digitos
    t2=int(usuario[-2]) # penultimo digito para ops
    n1,n2,n3=(int(t1[0]),int(t1[1]),int(t1[2])) #obtenemos los 3numeros para operaciones

    if (inpass==egg):
        listlat=[]
        numerolat=input("Ingrese el numero de latitudes que desea calcular. ")
        for l1 in range(0,int(numerolat)):          
            print("Ingrese la latitud {} : ".format(l1+1) )
            listlat.append(float(input("")))
        average=sum(listlat)/len(listlat)
        print("El promedio es: {}".format(average))
        exit()


    # operaciones matematicas
    if (n1*n2*n3==t2 or (n1+n2)%n3==t2 or abs(n1-n2)==t2 or abs(n1-n3)==t2 or (n1%n2)+n3==t2):
        n4=t2
        tr=int(t1)+n4
        if (str(tr)==input("Captcha "+str(t1)+'+'+str(t2)+':')):
            print("Sesión iniciada")
            # menu ppal
            nc=True  # variable para saber si el usuario ya ingreso coordenadas
            listamenu=["Cambiar contraseña", "Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana" , "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión"]  
            # sesssion loop
            mistakes=0
            while mistakes<3:                        
                for i in range(len(listamenu)):
                    if i==0:
                        print("\nMenu principal")
                    print(str(i+1)+'.'+listamenu[i]) # menu ppal                
                opcion=input("\nElija una opción:") 
                if (opcion.isnumeric()):
                    if(int(opcion)==2022):
                                            latituding=float(input("Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario."))  
                                            if latituding>-81.296 and latituding<-67.401:  
                                                print("El huso horario es -5") 
                                            elif latituding>-67.402 and latituding<-54.316:  
                                                print("El huso horario es -4") 
                                            elif latituding>-54.316 and latituding<-35.833:  
                                                print("El huso horario es -3") 
                                            else: print("huso desconocido") 
                                            break




                    if (int(opcion)>0 and int(opcion)<8 ):
                        if (listamenu[int(opcion)-1]=="Cambiar contraseña"):
                            print("Usted ha elegido la opción número ", opcion ) 
                            if (contraseña==input("Ingrese la contraseña actual:")):
                                newcontraseña=input("Nueva contraseña:") 
                                if (newcontraseña==contraseña):
                                    print('Error contraseña debe ser diferente a la anterior')
                                else: contraseña=newcontraseña;print('Contraseña cambiada con exito.')
                            else: print('Error contraseña mal ingresada.'); break                       
                            # print('Contraseña guardada con exito')
                            mistakes=0 # para mantener la session
                        elif (listamenu[int(opcion)-1]=="Ingresar coordenadas actuales"):
                            print("Usted ha elegido la opción número ", opcion ) 
                            # coordenadas grados. 3 decimales.
                            # latitud, longitud. deben quedar en una matriz de 3filas(casa, trabajo, parque) 2 columnas(latitud, longitud)                            
                            # se debe verificar que esten en el rango latitud Sup: 2.766 Inf:2.548 longitud  Or:-76.493 Occ:-76.879
                            # si alguna coordenada queda vacia o no esta en el rango debe salir error y finalizar el programa
                            # coordenadas grados. 3 decimales.
                            #primer ingreso name=['Casa   ','Trabajo','Parque ']
                            if (nc):
                                Mcoord=creaM(3,2) #creamos la matrix
                                #validar las restricciones de coordenadas...
                                print("Ingresar coordenadas dentro del siguiente rango Latitud Inf:2.548  Sup: 2.766  longitud Or:-76.493 Occ:-76.879  " ) 
                                try:                                   
                                    Mcoord[0][0]=vallat(input("ingrese la latitud de la Casa:")) 
                                    Mcoord[0][1]=vallong(input("ingrese la longitud de la Casa:")) 
                                    Mcoord[1][0]=vallat(input("ingrese la latitud del Trabajo:")) 
                                    Mcoord[1][1]=vallong(input("ingrese la longitud del Trabajo:"))
                                    Mcoord[2][0]=vallat(input("ingrese la latitud del Parque:")) 
                                    Mcoord[2][1]=vallong(input("ingrese la longitud del Parque:"))
                                    nc=False
                                except: 
                                    print("Coordenadas erradas o no estan dentro del rango") 
                                    break                                                                           
                            #si el usuario vuelve a ingrear debera:                                                                                                  
                            elif (nc==False):
                                                                                                                              
                                 #indicar la coordenada mas ubicada al sur, coordenada promedio de latitud longitud de todos los puntos 
                                print('la coordenada mas al sur es '+ str(masalsur(Mcoord)))                            
                                print('Promedio Latitud,longitud: '+ str(promedioM(Mcoord)))                                   
                                dibuja3M(Mcoord) #mostrar las coordenadas ya ingresadas.
                                 # mostrar el msg presione 1 2 o 3 para actualizar la respectiva coordenada/ si seleciona una incorrecta error y se finaliza
                                 # las nuevas coordenadas deben cumplir con las restricciones anteriores.                               
                                try:
                                    actualizacion=input("presione 1 2 o 3 para actualizar la respectiva coordenada de la casa, trabajo o parque. 0 para cancelar : ") 
                                    actualizacion=int(actualizacion)       
                                    if (actualizacion>=1 and actualizacion<4):
                                        print("las coordenadas deben estar dentro del siguiente rango Latitud Inf:2.548  Sup: 2.766  longitud Or:-76.493 Occ:-76.879  " ) 
                                        if(actualizacion==1):
                                            Mcoord[0][0]=vallat(input("ingrese la latitud de la Casa:")) 
                                            Mcoord[0][1]=vallong(input("ingrese la longitud de la Casa:"))
                                        elif(actualizacion==2):
                                            Mcoord[1][0]=vallat(input("ingrese la latitud del Trabajo:")) 
                                            Mcoord[1][1]=vallong(input("ingrese la longitud del Trabajo:"))
                                        elif(actualizacion==3):
                                            Mcoord[2][0]=vallat(input("ingrese la latitud del Parque:")) 
                                            Mcoord[2][1]=vallong(input("ingrese la longitud del Parque:"))   
                                    elif(actualizacion==0): 
                                            print("coordenadas no actualizadas")              
                                    else: break    
                                except: 
                                    print("Error numero no reconocido") 
                                    break   


                            mistakes=0
                        elif (listamenu[int(opcion)-1]=="Ubicar zona wifi más cercana"):
                            print("Usted ha elegido la opción número ", opcion ) 
                            #El programa disponie de manera predefinida la ubicacion de 4 zonas wifi ,con su promedio de usuarios                   
                            
                            #el programa permite encontrar 2 zonas wifi mas cercanas a su ubicacion y saber en cual de estas hay menos personas conectadas
                            #salida distancia a los 2 puntos mas cercanos y el numero de usuarios conectados promedio 
                            #debe mostrar la informacion de menor a mayor usuarios conectados
                            #en caso de que el usuario no haya ingresado coordenadas previamente dbe aprecer "Error sin registro de coordenadas". break
                            if nc:
                                print("Error sin registro de coordenadas")
                                break
                            else:
                                dibuja3M(Mcoord) #mostrar las coordenadas ya ingresadas.
                                try:
                                    ubicacion=input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión:")
                                    ubicacion=int(ubicacion)
                                    if(ubicacion==1):
                                        cercanos=obtenermascercanos(Mcoord[0][0],Mcoord[0][1],Zonaswifi) #funcion que calculas las distancias y organiza de menor a mayor por personas  
                                    elif(ubicacion==2):
                                        cercanos=obtenermascercanos(Mcoord[1][0],Mcoord[1][1],Zonaswifi)        
                                    elif(ubicacion==3):
                                        cercanos=obtenermascercanos(Mcoord[2][0],Mcoord[2][1],Zonaswifi) 
                                    ubiok=True   #variable para saber que ya se tiene la ubicacion actual                                     
                                except: 
                                    print("Error ubicación") 
                                    break   

                            #si elige la opcion correcta debera realizar calcuo de distancia entre los puntos y mostrar los 2resultados de menor a mayor usuario prom conectados
                                print("Zona wifi 1 a {}M tiene conectadas {} personas".format(round(cercanos[0][0],2),cercanos[0][1]))
                                print("Zona wifi 2 a {}M tiene conectadas {} personas".format(round(cercanos[1][0],2),cercanos[1][1]))
                                try:
                                    indicaciones=input("eliga 1 o 2 para recibir indicaciones de llegada:")
                                    indicaciones=int(indicaciones)
                                    if(indicaciones==1):
                                        direccion(Mcoord[ubicacion-1][0],Mcoord[ubicacion-1][1],cercanos[0][0],cercanos[0][1])
                                        tiempop(cercanos[0][0])
                                    elif(indicaciones==2):
                                        direccion(Mcoord[ubicacion-1][0],Mcoord[ubicacion-1][1],cercanos[1][0],cercanos[1][1])
                                        tiempop(cercanos[1][0])
                                       
                            #El programa indica la direccion QUE DEBE SEGUIR del punto elegido Y cual es el tiempo promedio para llegar EN MOTO Y EN BICICLETA                       
                            #velocidad en bici 3.33m/s en moto 19.44m/s 

                                except: 
                                    print("Error zona wifi") 
                                    break 
                            
                            

                            mistakes=0
                        elif (listamenu[int(opcion)-1]=="Guardar archivo con ubicación cercana"):
                            print("Usted ha elegido la opción número ", opcion ) 
                            mistakes=0      
                            #datos organizados en formato diccioanrio apra ser exportados
                            #si no se tiene la ubicacion actual de las 3 debe salir error break
                            if ubiok:                           
                                informacion = {"actual": [Mcoord[ubicacion-1][0], Mcoord[ubicacion-1][1]],"zonawifi1": [cercanos[indicaciones-1][2], cercanos[indicaciones-1][3],cercanos[indicaciones-1][1]],"recorrido": [round(cercanos[indicaciones-1][0],3), 'bicicleta', round((cercanos[indicaciones-1][0]/3.33)/60,3)]}
                                print(informacion)   
                                                           
                                conf= int(input("esta de acuerdo con la info a exportar? presione 1 para confirmar, 0 para regresar al menu principal : "))
                                if conf==1:    
                                    sitios=['Casa','Trabajo','Parque ']# sitios frecuentes
                                    informacion["actual"].append(sitios[ubicacion-1])  # adicionamos el nombre del lugar actual                
                                    datos=pd.DataFrame(informacion)# creamos dataframe
                                    datos.to_csv('Info.csv', index=False)# exportamos al archivo
                                    print("Exportando archivo")  
                                    break
                                elif conf==0: 
                                    pass 
                            else: 
                                print("Error de alistamiento")
                                break
                        elif (listamenu[int(opcion)-1]=="Actualizar registros de zonas wifi desde archivo"):
                            print("Usted ha elegido la opción número ", opcion ) 
                            #archivo externo para actualizar registros de zonas wifi
                            #se debe leer un archivo externo con los datos de la matriz ubicaciones wifi
                            #msg Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menu principal                           
                            zy=pd.read_csv('Zwifi.csv') #leemos el archivo
                            print(zy)
                            zy.head()
                            Zonaswifi = zy.values.tolist()                           
                            try:
                                if 0==int(input("Datos de coordenadas para zonas wifi actualizadas, presione 0 para regresar al menu principal. ")):
                                    pass
                            except: 
                                    print("Error") 
                                    break
                            mistakes=0     
                        elif (listamenu[int(opcion)-1]=="Elegir opción de menú favorita"):
                            opcionf=input("Elija una opción favorita:")

                            if (int(opcionf)>=0 and int(opcionf)<6):
                                
                                if (4==int(input("Para confirmar por favor responda:Soy el numero de patas de un perro... la respuesta es:"))):
                                    print("correcto")
                                    if (3==int(input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es:"))):    
                                        print("correcto")    
                                        favorito=listamenu.pop(int(opcionf)-1) #sacamos el favorito
                                        listamenu.insert(0,favorito) # lo agregamos de primero
                                        mistakes=0 
                                    
                                else: print('Error')
                        elif (listamenu[int(opcion)-1]=="Cerrar sesión"):
                            #confirmacion=input("Estas seguro que desea salir, responda si/no?")
                            #if ('si'==confirmacion or 'SI'==confirmacion or 'Si'==confirmacion):
                                print('Hasta pronto.')
                                break

                    else: print('Error respuesta no entre las opciones')
                else: print('Error ingrese numeros.')
                mistakes+=1
                if mistakes>=3:
                    print('Sesión cerrada')
            
                














        else:  print("Error") 
    else:print("Error")    
else: print("Error")
