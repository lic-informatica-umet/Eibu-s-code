while True: # Crea mientras
    try: # Intentar el statement
        raise ValueError # Levanta un ValueError manual
    except ValueError: # crea la excepcion
        print("There was an exception") # Muestra que hubo una excepcion
        break # Termina el mientras cortando la ejecucion

'''
while True:
    try:
        tipo_aviso = int(input("Seleccion: "))
        if 1 < tipo_aviso > 2: 
            raise ValueError 
        break
    except ValueError:
        print("Por favor, elija entre la opcion 1 y 2") 
'''