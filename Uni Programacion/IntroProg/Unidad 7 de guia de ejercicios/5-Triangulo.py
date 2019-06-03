# Programa: Tipos de triangulos
# Fecha: 20/04/2019
# Autor: Agustin Arce

# Inicializacion de variables

lado1 = 0
lado2 = 0
lado3 = 0

# Ingreso de datos

lado1 = float(input("Ingrese primer lado: "))
lado2 = float(input("Ingrese segundo lado: "))
lado3 = float(input("Ingrese tercer lado: "))

# Control de Flujo

if lado1 == lado2:
    print("Es un triangulo isoceles.")
elif lado2 == lado3:
    print("Es un triangulo isoceles.")
elif lado1 == lado3:
    print("Es un triangulo isoceles.")
elif lado1 == lado2 == lado3:
    print("Es un triangulo equilatero.")
else:
    print("Es un triangulo escaleno.")