'''
Codificar un programa que permita los socios de club social el pago de sus cuotas a través
de internet. Para ello; el sistema deberá posibilitar el ingreso del monto a pagar, pudiéndose
pagar el total o parte de la cuota social cuyo monto mensual asciende los $1500.

Aclaraciones:
    • El sistema deberá informar el saldo a pagar (valor de la cuota descontado el pago realizado).
    • El monto a pagar podrá incluir centavos
'''

# Programa: Pago a club
# Nombre: Agustin Arce
# Fecha: 27/05/2019

# Inicializacion de variables

montoPagar = 0
cuotaMensual = 1500.00

# Ingreso de datos

print("El monto mensual a pagar es de:", cuotaMensual)
montoPagar = float(input("Ingrese monto que desea pagar: $"))

# Operacion

cuotaMensual = cuotaMensual - montoPagar

# Muestra de informacion

if cuotaMensual > 0:
    print("El monto restante a pagar es de: $", cuotaMensual)
elif cuotaMensual < 0:
    print("Ud. tiene un saldo a favor de: $", cuotaMensual)
else:
    print("Tu cuota fue saldada.")