'''
8. Ingresar los lados de un rectángulo y calcular su diagonal principal, superﬁcie, y perímetro. 
'''

# Fecha: 08/04/2019
# Autor: Agustin Arce
# Programa: Calculo de un rectangulo

# Inicializacion de variables

base = 0
altura = 0
hipotenusa = 0
perimetro = 0
superficie = 0 # Cuadrado

# Ingreso de datos

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

# Calculo de hipotenusa, perimetro y superficie

hipotenusa = (base**2 + altura**2)**0.5
perimetro = (base + altura) * 2
superficie = (base * altura)

# Muestra de informacion 

print("La diagonal vale: ", hipotenusa, ".")
print("El perimetro vale: ", perimetro, ".")
print("La superﬁcie vale: ", superficie, " cm2.")