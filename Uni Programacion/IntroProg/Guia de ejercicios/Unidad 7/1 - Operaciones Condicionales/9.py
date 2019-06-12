'''
9. Ingresar el valor de la hora y el tiempo trabajado por un empleado, calcular su sueldo si se sabe que recibe un premio de $ 100 si trabajo más dc 50 horas y si trabajo más de 150 horas le dan $100 adicionales. 
'''

# Fecha: 20/04/2019
# Autor: Agustin Arce
# Programa: Sueldo

# Definicion de constantes

PREMIO = 100
ADICIONAL = 100

# Inicializacion de variables

horas = 0
valor = 0
sueldo = 0

# Ingreso de datos

valor = float(input("Ingrese valor de la hora trabajada: "))
horas = int(input("Ingrese cantidad de horas trabajadas: "))

# Operacion

sueldo = horas * valor

# Control de flujo

if 50 <= horas <= 149:
    sueldo = sueldo + PREMIO
elif horas >= 150:
    sueldo = sueldo + PREMIO + ADICIONAL

# Muestra de informacion

print("El sueldo es de:", sueldo)