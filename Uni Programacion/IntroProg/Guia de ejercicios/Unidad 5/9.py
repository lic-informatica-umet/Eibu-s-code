'''
9. Ingresar dos valores, calcular su suma, su producto y la resta del 1ro menos el 2do. 
'''

# Fecha: 08/04/2019
# Autor: Agustin Arce
# Programa: Suma, producto y resta

# inicializacion de variables

numero1 = 0
numero2 = 0
suma = 0
producto = 0
resta = 0

# Muestra del uso del programa

print("Este programa muestra el resultade de la suma, el producto y a resta entre los dos numeros introducidos")

# Ingreso de datos

num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))

# Operaciones

suma = numero1 + numero2
producto = numero1 * numero2
resta = numero1 - numero2

# Muestra de resultados en pantalla

print("La suma de los dos valores es:", suma)
print("El producto entre los dos valores es:", producto)
print("La resta entre los dos valores es:", resta)