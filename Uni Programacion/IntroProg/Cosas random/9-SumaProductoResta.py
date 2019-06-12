# Programa: Suma, producto y resta
# Fecha: 08/04/2019
# Autor: Agustin Arce

# inicializacion de variables

num1 = 0
num2 = 0
suma = 0
prod = 0
resta = 0

# Muestra del uso del programa

print("Este programa muestra el resultade de la suma, el producto y a resta entre los dos numeros introducidos")

# Ingreso de datos

try:
    num1 = float(input("Ingrese primer numero: "))
except:
    print("No es un numero valido, sera tomado como 0")

try:
    num2 = float(input("Ingrese segundo numero: "))
except:
    print("No es un numero valido, sera tomado como 0")
# Operaciones

suma = num1 + num2

prod = num1 * num2

resta = num1 - num2

# Muestra de resultados en pantalla

print("La suma de los dos valores es:", suma)
print("El producto entre los dos valores es:", prod)
print("La resta entre los dos valores es:", resta)