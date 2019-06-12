'''
10. Ingresar tres valores correspondientes al día, mes y año de una fecha, indicar si es válida, considerar los años bisiestos. 
'''

# Fecha: 27/04/2019
# Autor: Agustin Arce
# Programa: Fecha valida

año = 0
mes = 0
dia = 0
año_es_bisiesto = False

while año == 0:
    año = int(input("Ingrese un año entre 1 y 3000: "))
    if año < 1 or año > 3000:
        print("Ingrese un valor entre 1 y 3000.")
        año = 0
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        año_es_bisiesto = True

    while mes == 0:
        mes = int(input("Ingrese un mes entre 1 y 12: "))
        if mes < 1 or mes > 12:
            print("Ingrese un valor entre 1 y 12.")
            mes = 0
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = int(input("Ingrese un dia entre 1 y 30:"))
        if dia < 1 or dia > 30:
            print("Ingrese un valor entre 1 y 30.")
            dia = 0
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dia = int(input("Ingrese un dia entre 1 y 31: "))
        if dia < 1 or dia < 31:
            print("Ingrese un valor entre 1 y 31.")
            dia = 0    
    if mes == 2 and año_es_bisiesto == False:
        while dia == 0:
            dia = int(input("Ingrese un dia entre 1 y 28: "))
            if  dia < 1 or dia > 28:
                print("Ingrese un valor entre 1 y 28.")
                dia = 0
    if mes == 2 and año_es_bisiesto == True:
        while dia == 0:
            dia = int(input("Ingrese un dia entre 1 y 29: "))
            if dia < 1 or dia > 29:
                print("Ingrese un valor entre 1 y 29.")
                dia = 0

    print("La fecha:", dia, "/", mes, "/", año,"es valida.")