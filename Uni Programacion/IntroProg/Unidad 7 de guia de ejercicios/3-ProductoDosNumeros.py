# Programa: Producto entre dos numeros
# Nombre: Agustin Arce
# Fecha: 20/04/2019

# Inicializacion de variables

num1 = 0
num2 = 0
prod = 0

# Ingreso de datos

num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))

# Operacion

prod = num1 * num2

# Control de flujo e informacion en pantalla

if num1 == num2:
    print("Los dos numeros son iguales, no se mostrara el producto")
elif num1 >= num2:
    print("El producto entre los dos valores es:", prod)
else:
    print("Intente indicar el primer numero como mayor")