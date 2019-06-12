'''
Codifique un programa que permita calcular el monto a pagar de la tarifa de luz, si sabe que
se pagan $300 como monto fijo, y que también se paga 10$ por KWH (Kilowatt Hora) consumido.
'''

# Programa: Calculo Electricidad
# Nombre: Agustin Arce
# Fecha: 27/05/2019

# Inicializacion de variables

kwhConsumo = 0
totalPagar = 0

# Declaracion de constantes

MONTOFIJO = 300
KWH = 10

# Ingreso de datos

kwhConsumo = float(input("Ingrese la cantidad de kWh consumidos: "))

# Operacion

totalPagar = (kwhConsumo * KWH) + MONTOFIJO

# Muestra de informacion

print("La suma a pagar es de: $", totalPagar)