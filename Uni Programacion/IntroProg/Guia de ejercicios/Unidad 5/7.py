'''
7. Ingresar los lados de un triángulo calcular su perímetro, Ingresar dos lados de un triángulo rectángulo y calcular, la hipotenusa, el perímetro, y la superﬁcie.
'''

# Fecha: 08/04/2019
# Autor: Agustin Arce
# Programa: Calculo del perimetro de un triangulo

# inicializacion de variables

base = 0
altura = 0
hipotenusa = 0
perimetro = 0
superficie = 0 # Cuadrado

# Ingreso de datos

base = float(input("Ingrese la base del triangulo rectangulo: "))
altura = float(input("Ingrese la altura del triangulo rectangulo: "))

# Calculo de hipotenusa, perimetro y superficie

hipotenusa = (base**2 + altura**2)**0.5
perimetro = base + altura + hipotenusa
superficie = (base * altura)/2

# Muestra de informacion 

print("La hipotenusa vale: ", hipotenusa, ".")
print("El perimetro vale: ", perimetro, ".")
print("La superﬁcie vale: ", superficie, " cm2.")