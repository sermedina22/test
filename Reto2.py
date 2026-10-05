# msg bienvenida
print("Bienvenido al sistema de ubicación para zonas públicas WIFI 51743 34715 747")
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
                            # contraseña=input("Nueva contraseña:") 
                            # print('Contraseña guardada con exito')
                            mistakes=0 # para mantener la session
                        elif (listamenu[int(opcion)-1]=="Ingresar coordenadas actuales"):
                            print("Usted ha elegido la opción número ", opcion ) 
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
