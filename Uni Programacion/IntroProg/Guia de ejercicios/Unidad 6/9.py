'''
9. Codificar un programa para que, a partir de un monto en pesos, se calcule su equivalente en dólares. 
'''

# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Pesos a dolares

# inicializacion de variables

pesos = 0
dolares = 0
pesosadolares = 0

# Ingreso de datos

pesos = float(input("Ingrese la cantidad de pesos a convertir: $"))
dolares = float(input("Ingrese el valor del dolar en pesos: $"))

# Operaciones

pesosadolares = pesos / dolares

# Mostrar el resultado

print(pesos, "pesos es igual a", pesosadolares, "dolares")