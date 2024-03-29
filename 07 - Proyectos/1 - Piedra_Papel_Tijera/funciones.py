from random import randint
#Opciones 
opciones = ["Piedra", "Papel", "Tijera"]
#Puntos, contador, condición para el bucle en main
puntos_jugador = 0
puntos_maquina = 0
c = 0
victoria=False
#Funcion que recibe el nombre del usuario
def RecibirNombre(nombre):
    global name
    name=nombre
#Función para corroborar si los jugadores ingresaron el mismo numero en caso contrario
#Se hace la comparación
def IgualdadOpciones(indice):
    global c, puntos_jugador, puntos_maquina
    indice_r = OpcionRobot()
    if opciones[indice] == opciones[indice_r]:
        print(" ")
        print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nEmpate, nadie se lleva punto\n")
    else:
        c += 1
        Comparacion(indice, indice_r)
        if c>=3:
            ComprobarVictoria(puntos_jugador,puntos_maquina)
#Función para recibir elección hecha por la cpu
def OpcionRobot():
    return randint(0, 2)
#Corrobora su hay un ganador
def ComprobarVictoria(puntos_jugador, puntos_maquina):
    global victoria
    if puntos_jugador == 3 or puntos_maquina == 3:
        if puntos_jugador == 3:
            print(f"{name} ganó. ¡Felicidades!")
            print(" ")
            victoria=True
        else:
            print("CPU ganó, mejor suerte la próxima!")
            print(" ")
            victoria=True
            
    return victoria
#Compara opciones de los jugadores y asigna los puntos
def Comparacion(indice, indice_r):
    global puntos_jugador, puntos_maquina
    if abs(indice - indice_r) == 1:
        if indice > indice_r:
            print(" ")
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para {name}")
            print(" ")
            puntos_jugador += 1
        else:
            print(" ")
            puntos_maquina += 1
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para CPU")
            print(" ")
    if abs(indice - indice_r) == 2:
        if indice > indice_r:
            print(" ")
            puntos_maquina += 1
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para CPU")
            print(" ")
        else:
            print(" ")
            puntos_jugador += 1
            print(f"Elección de {name}: {opciones[indice]}\n\nElección CPU: {opciones[indice_r]}\n\nPunto para {name}")
            print(" ")
#Función para resetear la condición de victoria en caso de que el jugador
#quiera jugar de nuevo
def ResetVictoria():
    global victoria,puntos_jugador,puntos_maquina
    puntos_jugador =0
    puntos_maquina =0
    victoria=False