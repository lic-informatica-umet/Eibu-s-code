while True: # Crea mientras
    try: # Intentar el statement
        raise ValueError # Levanta un ValueError manual
    except ValueError: # crea la excepcion
        print("There was an exception") # Muestra que hubo una excepcion