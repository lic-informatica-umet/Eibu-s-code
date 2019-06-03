# Programa: Ingresar la patente y monto de la multa de 50 autos, indicar cuantos montos superan los $40 y del total cobrado que porcentaje representa la suma de estos últimos.'''
# Fecha: 20/05/2019
# Autor: Agustin Arce

# Declaracion de constantes

LIMITE = 5

# Inicializacion de variables

patente = ""
ciclos = 0
montossup40 = 0
sumasmontossup40 = 0
totalcobrado = 0
monto = 0

# Ingreso de patente

patente = str(input("Ingrese patente: "))

# Mientras ciclos sea menor al limite de ciclos inpuestos
while (ciclos < LIMITE):
    monto = float(input("Ingrese monto de la multa: ")) # Pide un valor de multa
    if monto > 40: # Si supera los $40
        totalcobrado += monto
        sumasmontossup40 += monto
        montossup40 += 1
    elif monto <= 40: # Si no supera los $40
        totalcobrado += monto
    # Reestabecimiento de valor de monto y conteo de ciclo
    monto = 0
    ciclos += 1
    
print ("Los montos que superaron los $40 en la patente", patente, "son:", montossup40, "y representan un", sumasmontossup40 * 100 / totalcobrado , "'%' del monto total.")