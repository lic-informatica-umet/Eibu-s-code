'''
Codifique un programa que permita ingresar, la carrera de un alumno teniendo en cuenta la siguiente codificación:
A. Licenciatura en Gestión Operativa de Construcciones Inteligentes. 
B. Licenciatura en Informática  
C. Licenciatura en Economía 
 
Se necesita obtener: 
• La cantidad de alumnos de cada carrera. 
• La carrera que posee mayor cantidad de alumnos. 
• La carrera que posee menor cantidad de alumnos. 
• La cantidad total de alumnos de la universidad. 
• La cantidad de alumnos promedio de la universidad. 
'''

# inicializacion de variables

eleccion = ""
nombre = ""
cantidad_alumnos_A = 0
cantidad_alumnos_B = 0
cantidad_alumnos_C = 0
cantidad_alumnos_M = 0
carrera_mayor = ""
cantidad_alumnos_m = 0
carrera_menor = ""
cantidad_alumnos_T = 0
cantidad_alumnos_P = 0
continuar = 1

# Ingreso de datos, Control de flujo, bucle

# El primer mientras condiciona si desea continuar o no, la variable esta especificada en "s" al inicio para comenzar el bucle
while continuar == 1:

    # Se ingresa el nombre del alumno
    print("ingrese el nombre del alumno: ")
    while nombre == "":
        nombre = input()
        if nombre == "":
            print("Por favor ingrese un nombre.")
        
    # Muestra de elecciones de carreras
    print("Ingrese A para Licenciatura en Gestión Operativa de Construcciones Inteligentes.")
    print("Ingrese B para Licenciatura en Informatica.")
    print("Ingrese C para Licenciatura en Economia.")
    print("Ingrese eleccion de carrera:")
    while eleccion == "":
        eleccion = input()
        # Control de flujo y operaciones necesarias para los acumuladores
        if eleccion == "a":
            cantidad_alumnos_A = cantidad_alumnos_A + 1
            cantidad_alumnos_T = cantidad_alumnos_T + 1
            cantidad_alumnos_P = cantidad_alumnos_T / 3
        elif eleccion == "b":
            cantidad_alumnos_B = cantidad_alumnos_B + 1
            cantidad_alumnos_T = cantidad_alumnos_T + 1
            cantidad_alumnos_P = cantidad_alumnos_T / 3
        elif eleccion == "c":
            cantidad_alumnos_C = cantidad_alumnos_C + 1
            cantidad_alumnos_T = cantidad_alumnos_T + 1
            cantidad_alumnos_P = cantidad_alumnos_T / 3
        else:
            eleccion = ""
            print("Por favor seleccionar las carreras listadas con 'a', 'b' o 'c.")

        if cantidad_alumnos_A >= cantidad_alumnos_B or cantidad_alumnos_C:
            cantidad_alumnos_M = cantidad_alumnos_A + cantidad_alumnos_M
        elif cantidad_alumnos_B >= cantidad_alumnos_A or cantidad_alumnos_C:
            cantidad_alumnos_M = cantidad_alumnos_B + cantidad_alumnos_M
        elif cantidad_alumnos_C >= cantidad_alumnos_A or cantidad_alumnos_B:
            cantidad_alumnos_M = cantidad_alumnos_C + cantidad_alumnos_M

        if cantidad_alumnos_A <= cantidad_alumnos_B and cantidad_alumnos_C:
            cantidad_alumnos_m = cantidad_alumnos_A
        elif cantidad_alumnos_B <= cantidad_alumnos_A and cantidad_alumnos_C:
            cantidad_alumnos_m = cantidad_alumnos_B
        elif cantidad_alumnos_C <= cantidad_alumnos_A and cantidad_alumnos_B:
            cantidad_alumnos_m = cantidad_alumnos_C

    if cantidad_alumnos_M == cantidad_alumnos_A:
        carrera_mayor = "Licenciatura en Gestión Operativa de Construcciones Inteligentes."
    if cantidad_alumnos_M == cantidad_alumnos_B:
        carrera_mayor = "Licenciatura en Informatica."
    if cantidad_alumnos_M == cantidad_alumnos_C:
        carrera_mayor = "Licenciatura en Economia."

    if cantidad_alumnos_m == cantidad_alumnos_A:
        carrera_menor = "Licenciatura en Gestión Operativa de Construcciones Inteligentes."
    if cantidad_alumnos_m == cantidad_alumnos_B:
        carrera_menor = "Licenciatura en Informatica."
    if cantidad_alumnos_m == cantidad_alumnos_C:
        carrera_menor = "Licenciatura en Economia."

    # Muestra de informacion
    print("El alumno", nombre, "se a registrado.")
    print("La carrera con mayor cantidad de alumnos es:", carrera_mayor)
    print("La carrera con menor cantidad de alumnos es:", carrera_menor)
    print("El total de alumnos es de", cantidad_alumnos_T)
    print("La cantidad promedio de alumnos es", cantidad_alumnos_P)

    eleccion = ""
    nombre = ""
    continuar = ""
    
    while continuar == "":
        print("Desea continuar ingresando alumnos? S para continuar N para cancelar.")
        continuar = input()
        if continuar == "s":
            continuar = 1
        elif continuar == "n":
            continuar = 0
        else:
            print("ingrese 's' o 'n'.")
            continuar = ""