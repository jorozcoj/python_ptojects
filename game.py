#Este juego es: piedra, papel o tijera

import random

def choose_option():
    options = ('piedra', 'papel', 'tijera')
    user_option = input("ingrese una opción: piedra, papel o tijera: ")
    user_option = user_option.lower()

    if not user_option in options:
        print("The option is not valid")
        return None, None
        
    pc_option = random.choice(options)
    return user_option, pc_option

def check_rules(user_option, pc_option,victoria_usuario, victoria_pc):
    if user_option == pc_option:
        print ("La opcion de la computadora fue: ", pc_option)
        print("se produjo un empate")
        
    elif  user_option == 'piedra' and pc_option == 'tijera' or user_option == 'papel' and pc_option=='piedra' or user_option == 'tijera' and pc_option=='papel':
        print ("La opcion de la computadora fue: ", pc_option)
        print ("el usuario gana")
        victoria_usuario+=1
    else: 
        print ("La opcion de la computadora fue: ", pc_option)
        print("La computadora gana")
        victoria_pc+=1
    print ("victorias del pc =>" ,victoria_pc)
    print ("victorias del usuario =>" ,victoria_usuario)
    return victoria_usuario,victoria_pc

def choose_winner(victoria_usuario,victoria_pc): 
    if victoria_usuario ==2:
        print("el ganador es el usuario")
        exit()
    if victoria_pc == 2:
        print("gana la computadora")
        exit()
        

def start_game():    
    victoria_usuario=0
    victoria_pc =0
    juegos=1

    while True:
        choose_winner(victoria_usuario, victoria_pc)  

        print('-' * 10)
        print('juego # ', juegos)
        print('-' * 10)
        juegos +=1
        
        user_option,pc_option = choose_option()          

        victoria_usuario, victoria_pc=check_rules(user_option,pc_option,victoria_usuario,victoria_pc)  
                
start_game()