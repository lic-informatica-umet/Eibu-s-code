'''
Codificar un programa para una máquina expendedora de gaseosas que le permita elegir
de un menú de opciones entre gaseosa cola, gaseosa lima limón y agua tónica. El sistema
deberá informar que gaseosa eligió el usuario y cuál es el monto a pagar (IVA Incluido).

Se sabe que los precios de la gaseosa cola, gaseosa lima limón y agua tónica son $30, $35
y 40$ respectivamente (dichos precios no incluyen IVA).
'''

# Programa: Maquina expendedora
# Nombre: Agustin Arce
# Fecha: 27/05/2019 

# Inicializacion de variables

eleccion = 0 # Variable para elegir la gaseosa
cola = 30
lima_limon = 35
agua_tonica = 40
monto_Pagar = 0

# Declaracion de constante

IVA = 0.21 # IVA constante para multiplicar (21%)

# Ingreso de datos

print("Seleccione su gaseosa segun el numero:")
print("1 - Cola: $30.")
print("2 - Lima Limon: $35.")
print("3 - Agua Tonica: $40.")
print("(Los valores no incluyen IVA.)")

while eleccion == 0:
    eleccion = int(input())
    if eleccion < 1 or eleccion > 3:
        print("Numero invalido. Solo se puede seleccionar 1, 2 y 3.")
        eleccion = 0

# Control de flujo

if eleccion == 1:
    monto_pagar = cola + (cola * IVA)
    print("Ud. a selecionado una gaseosa Cola. Su costo con IVA es de: $", monto_pagar)
elif eleccion == 2:
    monto_pagar = lima_limon + (lima_limon * IVA)
    print("Ud. a selecionado una gaseosa Lima Limon. Su costo con IVA es de: $", monto_pagar)
elif eleccion == 3:
    monto_pagar = agua_tonica + (agua_tonica * IVA)
    print("Ud. a selecionado una gaseosa Agua Tonica. Su costo con IVA es de: $", monto_pagar)