# Programa: Indicar valor
# Fecha: 15/04/2019
# Autor: Agustin Arce

# Inicializacion de variables

num1 = 0

# Ingreso de datos

num1 = float(input("Ingrese numero: "))

# Control de flujo e informacion en pantalla

if num1 > 0:
    print("El numemro es positivo")
elif num1 < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")