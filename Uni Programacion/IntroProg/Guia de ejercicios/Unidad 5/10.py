'''
10. Ingresar el valor de la hora y el tiempo trabajado por un operario, calcular su sueldo.
'''

# Fecha: 08/04/2019
# Autor: Agustin Arce
# Programa: Horario Trabajado

# inicializacion de variables

valor_hora = 0
horas_trabajadas = 0
sueldo = 0

# Ingreso de datos

valor_hora = float(input("Ingrese valor a pagar por hora trabajada: "))
horas_trabajadas = float(input("ingrese las horas trabajadas: "))

# Operacion de calculo

sueldo = valor_hora * horas_trabajadas # Multiplicacion de la hora trabajada por el valor de la hora

# Muestra de resultados

print("Su sueldo debe ser de: $", sueldo)