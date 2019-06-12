'''
Una compañía de alquiler de vehículos autónomos desea u programa para emitir las
facturas de sus clientes, teniendo en cuenta los siguientes puntos:
    • Si no superan los 300km de cantidad fija se cobran $5.000
    • De más de 300km hasta 1000 km se cobran $5000 + kilometraje a razón de 30$ por km.

Si se superan los 1000km se cobran $5000 + kilometraje a razón de $30 para las
distancias comprendidas entre 300 y 1000km, y $20 para las distancias mayores de
1000km.
'''

# Programa: Alquiler de vehiculos
# Nombre: Agustin Arce
# Fecha: 27/05/2019

# Inicializacion de variables

kmRecorridos = 0
total = 0

# Ingreso de datos

kmRecorridos = float(input("Ingrese los kilometros reocrridos: "))

# Control de flujo

if kmRecorridos <= 300:
    total = 5000
elif 301 <= kmRecorridos <= 1000: # Chequea si la variable comprende entre los dos valores
    total = (kmRecorridos * 30) + 5000
elif kmRecorridos >= 1001:
    total = (kmRecorridos * 20) + 5000

# Redondeo si el numero flotante da mas de 2 decimales

round(total, 2)

# Muestra de mensaje

print("El valor a pagar por el recorrido es de: $", total)