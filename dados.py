from random import randint

def insertar_nombre():
    jugador1= input("ingrese su nombre: ")
    jugador2= input("ingrese su nombre: ")
    return jugador1, jugador2

def seleccion_dados():
    dado1J1 = randint(1,6)
    dado2J1 = randint(1,6)
    dado1J2 = randint(1,6)
    dado2J2 = randint(1,6)

    return dado1J1,dado2J1,dado1J2,dado2J2
    
def revision_reglas(jugador1,jugador2,dado1J1,dado2J1,dado1J2,dado2J2,victorias_J1,victorias_J2):
    sumaDadosJ1=dado1J1+dado2J1
    sumaDadosJ2=dado1J2+dado2J2

    if sumaDadosJ1 == sumaDadosJ2:
        print("Esto es un empate")
    elif sumaDadosJ1 > sumaDadosJ2:
        print(f"{jugador1} sacó {sumaDadosJ1}, {jugador2} sacó {sumaDadosJ2}, {jugador1} ganó")
        victorias_J1+=1
    else:
        print(f"{jugador2} sacó {sumaDadosJ2}, {jugador1} sacó {sumaDadosJ1}, {jugador2} ganó")
        victorias_J2+=1
    return victorias_J1,victorias_J2

def elegir_ganador(jugador1,jugador2,victorias_J1,victorias_J2):
    if victorias_J1==3:
        print(f"El ganador fue {jugador1}")
        exit()
    if victorias_J2==3:
        print(f"El ganador fue {jugador2}")       
        exit()

def iniciar_juego():
    victorias_J1 = 0
    victorias_J2 = 0
    juegos=1
    jugador1,jugador2=insertar_nombre()

    while True:             
        
        elegir_ganador(jugador1,jugador2,victorias_J1,victorias_J2)    
        dado1J1,dado2J1,dado1J2,dado2J2=seleccion_dados()
        
        print("-" * 10)
        print("juego # ", juegos)
        print("-" * 10)
        print(f"dados {jugador1} : {dado1J1} , {dado2J1} ")
        print(f"dados {jugador2} : {dado1J2} , {dado2J2} ")
        juegos+=1        
        
        victorias_J1,victorias_J2 = revision_reglas(jugador1,jugador2,dado1J1,dado2J1,dado1J2,dado2J2,victorias_J1,victorias_J2)        

iniciar_juego()