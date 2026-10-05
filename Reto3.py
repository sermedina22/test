
#funciones utilizadas
def creaM(n,m):
    matriz = []
    for i in range(n):
        a = [0.000]*m
        matriz.append(a)
    return matriz

def dibuja3M(M):
    name=['Casa   ','Trabajo','Parque ']
    print("Coordenadas Actuales")
    for i in range(len(M)):
        print (str(name[i]) +' '+  str(M[i]))


def promedioM(M):
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




#  msg bienvenida
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario='51743'
contraseña=usuario[::-1] #usuario alreves
if (usuario==input("Nombre de usuario:")) and contraseña==input("Contraseña:"):   
    t1=usuario[2:5] # ultimos 3 digitos
    t2=int(usuario[-2]) # penultimo digito para ops
    n1,n2,n3=(int(t1[0]),int(t1[1]),int(t1[2])) #obtenemos los 3numeros para operaciones
    # operaciones matematicas
    if (n1*n2*n3==t2 or (n1+n2)%n3==t2 or abs(n1-n2)==t2 or abs(n1-n3)==t2 or (n1%n2)+n3==t2):
        # print("operations sucess")
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
                                    actualizacion=input("presione 1 2 o 3 para actualizar la respectiva coordenada de la casa, trabajo o parque. 0 para cancelar. ") 
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
                            mistakes=0
                        elif (listamenu[int(opcion)-1]=="Guardar archivo con ubicación cercana"):
                            print("Usted ha elegido la opción número ", opcion ) 
                            mistakes=0        
                        elif (listamenu[int(opcion)-1]=="Actualizar registros de zonas wifi desde archivo"):
                            print("Usted ha elegido la opción número ", opcion ) 

                            
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
                            confirmacion=input("Estas seguro que desea salir, responda si/no?")
                            if ('si'==confirmacion or 'SI'==confirmacion or 'Si'==confirmacion):
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
