# constantes

CBAR = 1000
CIGUAZU = 1500
CUSH = 3000

# variables

cantidad = 0
destino = -1
cantbar = 0
cantiguazu = 0
cantush = 0
montobar = 0
montoiguazu = 0
montoush = 0
momntototal = 0

####

while destino != 0:
    while destino < 0 or destino > 3:
        print("ingrese destino")
        destino = int(input())
        if destino < 0 or destino >3:
            print("error")

    if destino != 0:
        while cantidad < 1:
            print("ingrese cantidad")
            cantidad = int(input())
            if cantidad < 1:
                print("error")
        if destino == 1:
            cantbar += cantidad
        elif destino == 2:
            cantiguazu += cantidad
        elif destino == 3:
            cantush += cantidad
        
        destino = -1
        cantidad = -1

montobar = cantbar*CBAR
montoiguazu = cantiguazu*CIGUAZU
montoush = cantush*CUSH
momntototal = montobar+montoiguazu+montoush
#TODO: revisar comparaciones
if cantbar > cantiguazu and cantbar > cantush:
    print("Bariloche")
elif cantiguazu > cantbar and cantiguazu > cantush:
    print("Iguazu")
elif cantush > cantiguazu and cantush > cantbar:
    print("Ushuaia")
else:
    print("No hay maximos")

print(cantbar)
print(cantiguazu)
print(cantush)
print(montobar)
print(montoiguazu)
print(montoush)
print(momntototal)