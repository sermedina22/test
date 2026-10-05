from random import choice
palabrasecreta = None
progress = None
start = False
puntos_pc = 0
puntos_humano = 0
intentos = 0

matrix=[] #matrix 5x5
#palabras adivinar
actores = ["al pacino","Keanu reeves","scarlett johansson","Gal Gadot",""]
frutas = ["kiwi","pera","manzana","fresa", "mandarina"]
deportes = ["futbol","voleibol","tennis","natacion", "boxeo" ]
paises = ["colombia","estados unidos","francia", "australia", "mexico"]
generos = ["rock","salsa","reggae","metal","reggaeton"]
#creamos la matrix
matrix.append(actores)
matrix.append(frutas)
matrix.append(deportes )
matrix.append(paises)
matrix.append(generos)

#funcion para calcular la palabra adivinar
def aleatoria(categoria):
    pselecionada=choice(matrix[categoria])
    return pselecionada

def imprimirahorcado(errores):
    if errores == 1:
        print("____")
        print(" O  |")
        print("    |")
        print("   /_\\")
    elif errores == 2:
        print("  ____")
        print("  O   |")
        print("  |   |")
        print("     /_\\")
    elif errores == 3:
        print("  ____")
        print("  O   |")
        print(" -|   |")
        print("     /_\\")
    elif errores == 4:
        print("  ____")
        print("  O   |")
        print(" -|-  |")
        print("     /_\\")
    elif errores == 5:
        print("  ____")
        print("  O   |")
        print(" -|-  |")
        print(" /   /_\\")
    elif errores == 6:
        print("  ____  lastchance")
        print("  O   |")
        print(" -|-  |")
        print(" / \\  /_\\")
    elif errores >= 7:
        print("  ____")
        print("  |    |")
        print(" O*    |")
        print(" -|-   |")
        print(" / \\  /_\\")


def gameon(palabrasecreta):
    global puntos_pc
    global puntos_humano
    global progress
    global intentos
    letra = None
    temp = None
    cont = 0   
    palabrasecreta = palabrasecreta.lower()
    progress = (len(palabrasecreta)*"_ ").split()
    print(" ".join(progress))
    while True:
        letra = input("Ingrese una letra ")
        if len(letra)==1:
            if palabrasecreta.find(letra)!=-1:
                temp = ""
                cont = 0
                for i in palabrasecreta:
                    if i == letra:
                        progress[cont] = i
                    cont += 1
                print(" ".join(progress))
                if "".join(progress) == palabrasecreta:
                    print("¡Gano!")
                    puntos_humano = puntos_humano + 1
                    break 
            else:
                intentos = intentos + 1
                if intentos == 7:
                    imprimirahorcado(intentos)
                    print("Perdio")
                    puntos_pc = puntos_pc + 1
                    break
                else:
                    imprimirahorcado(intentos)
        else:
            print("Letra no valida") 

    intentos = 0

def imprimir_puntaje():
    global puntos_humano,puntos_pc
    imprimirahorcado(intentos)
    print("El puntaje es","\nHumano",puntos_humano,"\nComputador",puntos_pc)

while True:
    opcion = input("Seleccione la categoria asi:\n1. Actores\n2. Frutas\n3. Deportes\n4. Paises\n5. Generos musicales \n6. Salir\n>") 
    if opcion == "1":
        palabrasecreta = aleatoria(0)
    if opcion == "2":
        palabrasecreta = aleatoria(1)
    if opcion == "3":
        palabrasecreta = aleatoria(2)  
    if opcion == "4":
        palabrasecreta = aleatoria(3)
    if opcion == "5":
        palabrasecreta = aleatoria(4)
    if opcion == "6":
        break 
    gameon(palabrasecreta)
    imprimir_puntaje()

    input("Presione enter para continuar")