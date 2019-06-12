'''
8. Ingresar la edad y la altura de dos personas, indicar la estatura del de mayor edad. 
'''

# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Estatura del mayor

# Inicializacion de variables

altura1 = 0
edad1 = 0
altura2 = 0
edad2 = 0

# Ingreso de datos

# Persona 1

altura1 = float(input("Ingrese la altura de la primera persona: "))
edad1 = int(input("Ingrese edad de la primera persona: "))

# Persona 2

altura2 = float(input("Ingrese la altura de la segunda persona: "))
edad2 = int(input("Ingrese edad de la segunda persona: "))

# Control de flujo y muestra de informacion en pantalla

if edad1 > edad2:
    print("La altura de la persona mayor es:", altura1)
elif edad1 < edad2:
    print("La altura de la persona mayor es:", altura2)
else:
    print("Las dos personas tiene la misma edad, se mostraran las dos alturas:\n", 
        "La primera persona mide:", altura1, 
        "\n La segunda persona mide:", altura2)