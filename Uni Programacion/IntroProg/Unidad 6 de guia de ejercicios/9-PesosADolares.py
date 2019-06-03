# Programa: Pesos a dolares
# Fecha: 15/04/2019
# Autor: Agustin Arce

# inicializacion de variables

pesos = 0
dolares = 0
pesosadolares = 0

# Ingreso de datos

pesos = float(input("Ingrese la cantidad de pesos a convertir: $"))
dolares = float(input("Ingrese el valor del dolar en pesos: $"))

# Operaciones

pesosadolares = pesos / dolares

# Redondeo

pesosadolares = round(pesosadolares, 2)

# Mostrar el resultado

print(pesos, "pesos es igual a", pesosadolares, "dolares")