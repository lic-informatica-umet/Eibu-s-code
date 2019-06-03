# Programa: Promedios
# Fecha: 20/04/2019
# Autor: Agustin Arce

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
maxnota = max(nota1, nota2, nota3) # max() elije el maximo valor entre las variables

# Muestra de informacion

print("La nota maxima es:", maxnota)
print("El promedio de las notas es:", promedio)