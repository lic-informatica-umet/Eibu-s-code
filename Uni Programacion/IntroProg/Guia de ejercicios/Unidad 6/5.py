'''
5. Codificar un programa para que a partir de un número entero se calcule su resto.  
'''

# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Resto

# inicializacion de variables

num1 = 0
num2 = 0
resto = 0

# Ingreso de datos

num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))

# Operaciones

resto = num1 % num2

# Mostrar el resultado

print("El resto de la division entre los dos numeros es:", resto)