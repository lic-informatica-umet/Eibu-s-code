# Programa: Ingresos Brutos
# Fecha: 15/04/2019
# Autor: Agustin Arce

# inicializacion de variables

montoFacturado = 0
montoIngBrutos = 0
valorIngBrutos = 0

# Declaracion de constantes

INGBRUTOS = 0.03

# Ingreso de datos

montoFacturado = float(input("Ingrese monto facturado en pesos: $"))

# Operaciones

valorIngBrutos = montoFacturado * INGBRUTOS
montoIngBrutos = montoFacturado - valorIngBrutos

# Redondeo

montoIngBrutos = round(montoIngBrutos, 2)
valorIngBrutos = round(valorIngBrutos, 2)

# Mostrar el resultado

print("Los ingresos son de: $", montoIngBrutos)
print("El impuesto a los ingresos brutos es de: $", valorIngBrutos)