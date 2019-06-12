# Programa: Suma de dos numeros
# Fecha: 01/04/2019
# Autor: Agustin Arce

# inicializacion de variables
num1 = num2 = sum1 = 0 # al poner los iguales declaro todas las variables como 0, ahorrando lineas de codigo y tiempo de ejecucion

# Ingreso de datos
try: # inicia la excepcion
    num1 = int(input("Ingrese primer numero a sumar: ")) # int(input()) declara que el input solo puede ser un int
except: # si existe...
    print("No es un numero valido, sera tomado como 0") # muestra que no es valido
try:
    num2 = int(input("ingrese segundo numero a sumar: "))
except:
    print("No es un numero valido, sera tomado como 0")

# Operacion de suma
sum1 = num1 + num2

# Muestra resultado en pantalla
print("La suma es", sum1) # <-- , concatena el string con la variable