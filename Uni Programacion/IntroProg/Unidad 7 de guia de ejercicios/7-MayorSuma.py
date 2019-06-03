# Programa: Valor de suma mas alta
# Fecha: 20/04/2019
# Autor: Agustin Arce

# Inicializacion de variables

num1 = 0
num2 = 0
num3 = 0
num4 = 0
resultado1 = 0
resultado2 = 0

# Muestra de que hace el programa

print("Se sumara el primer valor con el segundo valor y el tercer valor con el cuarto valor.\n" 
    "Se mostrara la suma que de el resultado mas alto.")

# Ingreso de datos

num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))
num3 = float(input("Ingrese tercer numero: "))
num4 = float(input("Ingrese cuarto numero: "))

# Operaciones

resultado1 = num1 + num2
resultado2 = num3 + num4

# Control de flujo

if resultado1 > resultado2:
    print("El valor de la suma mas alta es:", resultado1)
elif resultado1 < resultado2:
    print("El valor de la suma mas alta es:", resultado2)
else:
    print("Los resultados son iguales.")