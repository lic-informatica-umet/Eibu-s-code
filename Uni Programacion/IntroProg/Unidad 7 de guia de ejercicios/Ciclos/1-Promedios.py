# Programa: Calcular promedio de 25 notas
# Autor: Agustin Arce
# Fecha: 20/05/2019

# Declaracion de Variables

nota, sumanota, ciclos = 0, 0, 0

'''
nota = 0 # Nota a ingresar
sumanota = 0 # Suma de notas
ciclos = 0 # Contador de cantidad de ciclos
'''

while ciclos < 25: # Mientras la cuenta de ciclos sea menor a la cantidad de notas a ingresar...
    nota = float(input("Ingrese la nota: ")) # Ingreso de la nota
    if nota < 0 or nota > 10:
        print("Por favor ingrese un valor entre 1 y 10")
    sumanota += nota #Suma de la nota ingresada con el resto de las notas
    ciclos += 1 # Conteo de ciclios
else:
    print("El promedio de las 25 notas ingresadas es:", sumanota / 25) # Impresion de la suma dividido por la cantidad de notas