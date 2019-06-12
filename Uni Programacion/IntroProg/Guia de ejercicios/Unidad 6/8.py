'''
8. Codificar un programa para que, a partir de la distancia recorrida por un vehículo en kilómetros, calcule el equivalente en millas. 
'''

# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Km a Millas

# inicializacion de variables

kilometros = 0
millas = 0

# Ingreso de datos

kilometros = float(input("Ingrese la distancia recorrida en kilometros: "))

# Operaciones

millas = kilometros * 0.621371

# Mostrar el resultado

print("La distancia recorrida en millas es de :", millas)