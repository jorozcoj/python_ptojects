import main

print(main.data) 
#Si lo importamos y no lo ejecutamos, no se ejecuta por si solo, solo se importa data

main.run()
#se controla la ejecución si se ejecuta esa linea 

#Example.py controla la ejecución de main.py, pero si desde la terminal tratamos de 
#ejecutar main.py no va a funcionar
#A eso se le llama dualidad
#para solucionarlo se agrega la siguiente linea en main if __name__ == '__main__: run()'