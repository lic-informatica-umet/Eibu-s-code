#determinar triangulo
#AUTOR lopez diego
#fecha 29/04/2019
 
#inicializacion de variables
lado1=0.00
lado2=0.00
lado3=0.00

#entrada de datos
print ("ingrese lado 1")
lado1=float(input())
print ("ingrese lado 2")
lado2=float(input())
print ("ingrese lado 3")
lado3=float(input())

#calculo
if lado1==lado2:
    if lado2==lado3:
        print ("equilatero")
if lado1==lado2:
      print ("isosceles")

if lado1==lado3:
      print ("isosceles")


if lado2==lado3:
      print ("isosceles")
else:
    print("escaleno")

        
