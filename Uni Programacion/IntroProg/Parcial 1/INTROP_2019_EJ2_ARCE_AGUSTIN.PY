# Programa: Ejercicio practico 2
# Autor: Agustin Arce Martinez
# Fecha: 29/04/2019

# Inicializacion de variables

lado1 = 0
lado2 = 0
lado3 = 0

# Ingreso de datos

lado1 = float(input("Ingrese valor del primer lado: "))
lado2 = float(input("Ingrese valor del segundo lado: "))
lado3 = float(input("Ingrese valor del tercer lado: "))

# Control de flujo y muestra de informacion

if lado1 == lado2 == lado3:
    print("El triangulo es equilatero.")
elif lado1 == lado2:
    print("El triangulo es isoceles.")
elif lado1 == lado3:
    print("El triangulo es isoceles.")
elif lado2 == lado3:
    print("El triangulo es isoceles.")
else:
    print("El triangulo es escaleno.")