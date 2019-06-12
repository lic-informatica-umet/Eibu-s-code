'''
4. Ingresar dos valores y realizar la resta del mayor menos el menor A 
'''

# Fecha: 20/04/2019
# Autor: Agustin Arce
# Programa: Resta del menor al mayor

# Inicializacion de variables

num1 = 0
num2 = 0
resta = 0

# Ingreso de datos

num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))

# Control de flujo

if num1 > num2:
    resta = num1 - num2
    print("La resta del mayor con el menor es:", resta)
elif num1 < num2:
    resta = num2 - num1
    print("La resta del mayor con el menor es:", resta)
else:
    print("Los numeros son iguales")