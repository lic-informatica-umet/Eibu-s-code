'''
6. Ingresar tres valores, sumarlos, calcular el promedio e indicar cuál de estos valores es mayor al promedio.
'''

# Fecha: 20/04/2019
# Autor: Agustin Arce
# Programa: Promedios

# Inicializacion de variables

nota1 = 0
nota2 = 0
nota3 = 0
promedio = 0
maxnota = 0

# Ingreso de datos

nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

# Operacion de promedio

promedio = (nota1 + nota2 + nota3) / 3

if nota1 > nota2 and nota3:
    maxnota = nota1
if nota2 > nota1 and nota3:
    maxnota = nota2
if nota3 > nota1 and nota2:
    maxnota = nota3

# Muestra de informacion

print("La nota maxima es:", maxnota)
print("El promedio de las notas es:", promedio)