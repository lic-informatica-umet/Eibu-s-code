'''
11. Ingresar el tiempo trabajado por un operario y si el valor de la hora es de 10 pesos, calcular su sueldo. 
'''

# Fecha: 08/04/2019
# Programa: Horario Trabajado V2
# Autor: Agustin Arce

# inicializacion de variables

valor_hora = 10
horas_trabajadas = 0
sueldo = 0

# Ingreso de datos

horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

# Operacion de calculo

sueldo = valor_hora * horas_trabajadas # Multiplicacion de la hora trabajada por el valor de la hora

# Muestra de resultados

print("Su sueldo debe ser de: $", sueldo)