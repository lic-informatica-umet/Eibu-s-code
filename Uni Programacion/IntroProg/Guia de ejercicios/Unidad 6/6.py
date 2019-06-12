'''
6. Codificar un programa para que a partir de un número entero se calcule su cociente. 
'''
# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Cociente

# inicializacion de variables

num1 = 0
num2 = 0
cociente = 0

# Ingreso de datos

num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))

# Operaciones

cociente = num1 // num2

# Mostrar el resultado

print("El cociente de la division entre los dos numeros es:", int(cociente)) # Transformarlo a integro redondea el flotante