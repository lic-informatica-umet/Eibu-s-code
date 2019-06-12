# Programa: Suma de tres valores V2
# Fecha: 08/04/2019
# Autor: Agustin Arce

# inicializacion de variables

num1 = num2 = num3 = sum1 = 0 # Igualacion de variables a 0

# Ingreso de datos

try: # Inicio de excepcion
    num1 = int(input("ingrese primer numero a sumar: ")) # Muestra mensaje y toma el input del teclado (solo int)
except: # Si no es int...
    print("No es un numero valido, sera tomado como 0") # muestra mensaje de error

try:
    num2 = int(input("ingrese segundo numero a sumar: "))
except:
    print("No es un numero valido, sera tomado como 0")

try:
    num3 = int(input("ingrese tercer numero a sumar: "))
except:
    print("No es un numero valido, sera tomado como 0")

# Operacion de suma

sum1 = num1 + num2 + num3 # Suma de numero uno y dos

# Muestra resultado en pantalla
print("La suma de los tres valores es:", sum1) # Muestra el resultado en pantalla