# msg bienvenida
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
        else:  print("Error") 
    else:print("Error")    
else: print("Error")
