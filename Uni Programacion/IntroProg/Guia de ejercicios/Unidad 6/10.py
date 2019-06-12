'''
10. Codificar un programa para que a partir del sueldo bruto (incluidos impuestos) calcule: 
a. El monto de obra social (3% del sueldo bruto) 
b. El monto de jubilación (11% del sueldo bruto) 
c. El monto de cuota sindical (1% del sueldo bruto) 
d. El sueldo neto (sueldo bruto con los descuentos anteriores). 
e. Muestre todos los conceptos anteriores por pantalla. 
'''

# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Calculo de sueldo

# inicializacion de variables

sueldoBruto = 0
obraSocial = 0
jubilacion = 0
cuotaSindical = 0
sueldoNeto = 0

# Ingreso de datos

sueldoBruto = float(input("Ingrese sueldo bruto a calcular neto: $"))

# Operaciones

obraSocial = (sueldoBruto * 3) / 100
jubilacion = (sueldoBruto * 11) / 100
cuotaSindical = (sueldoBruto * 1) / 100
sueldoNeto = sueldoBruto - obraSocial - jubilacion - cuotaSindical

# Mostrar el resultado

print("A partir del sueldo bruto: $", sueldoBruto)
print("Su sueldo neto es de: $", sueldoNeto)
print("El costo de la obra social es de: $", obraSocial)
print("El costo de la jubilacion es de: $", jubilacion)
print("El costo de la cuota sindical es de: $", cuotaSindical)