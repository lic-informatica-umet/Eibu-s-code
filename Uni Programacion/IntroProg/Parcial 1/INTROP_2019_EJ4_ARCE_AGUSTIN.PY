# Programa: Ejercicio practico 4
# Autor: Agustin Arce Martinez
# Fecha: 29/04/2019

# Declaracion de constantes

COSTO_FIJO_LINEAS = 100 # Costo fijo si se elijen el aviso por linea
COSTO_FIJO_POR_LINEA = 350  # Costo fijo por linea

AVISO_NOTABLE_2X5 = 1000 # Costo por eleccion de aviso notable 2x5
AVISO_NOTABLE_MEDIAPAGINA = 5000 # Costo por eleccion de aviso de media pagina
AVISO_NOTABLE_PAGINA = 10000 # Costo por eleccion de aviso de pagina completa

COMISION = 0.1765

# Inicializacion de variables

tipo_aviso = 0 # Eleccion del tipo de aviso
tipo_aviso_notable = 0 # Eleccion de tipo de aviso notable

cantidad_de_lineas = 0 # Cantidad de lineas por el aviso por linea

costo_total = 0 # Costo total de la publicacion
comision_total = 0 # Costo de la comision (17.65%)
total_a_abonar =0 # Total a pagar por el cliente

# Ingreso de datos y control de flujo

print("Elija las opciones definidas:")
print("1 - Aviso por linea.")
print("2 - Avisto notable.")
while True:
    try:
        tipo_aviso = int(input("Seleccion: "))
        if 1 < tipo_aviso > 2: 
            raise ValueError 
        break
    except ValueError:
        print("Por favor, elija entre la opcion 1 y 2") 

if tipo_aviso == 1:
    cantidad_de_lineas = int(input("Indique la cantidad de lineas: "))
    costo_total = COSTO_FIJO_LINEAS + (COSTO_FIJO_POR_LINEA * cantidad_de_lineas)
    comision_total = costo_total * COMISION
    total_a_abonar = costo_total + comision_total
    print("El costo total de la publicaion es de: ", costo_total)
    print("La comision es de: ", comision_total)
    print("El total a pagar es de: ", total_a_abonar)

if tipo_aviso == 2:
    print("Elija las opciones definidas:")
    print("1 - Aviso 2x5.")
    print("2 - Aviso de media pagina.")
    print("3 - Aviso de pagina entera.")
    while True:
        try:
            tipo_aviso_notable = int(input("Seleccion: "))
            if 1 < tipo_aviso_notable > 3:
                raise ValueError
            break
        except ValueError:
            print("Por favor, elija entre las opciones 1, 2 y 3.")

if tipo_aviso_notable == 1:
    costo_total = AVISO_NOTABLE_2X5
    comision_total = costo_total * COMISION
    total_a_abonar = costo_total + comision_total
    print("El costo total de la publicacion es de:", costo_total)
    print("La comision es de: ", comision_total)
    print("El total a pagar es de:", total_a_abonar)
elif tipo_aviso_notable == 2:
    costo_total = AVISO_NOTABLE_MEDIAPAGINA
    comision_total = costo_total * COMISION
    total_a_abonar = costo_total + comision_total
    print("El costo total de la publicacion es de:", costo_total)
    print("La comision es de: ", comision_total)
    print("El total a pagar es de:", total_a_abonar)
elif tipo_aviso_notable == 3:
    costo_total = AVISO_NOTABLE_PAGINA
    comision_total = costo_total * COMISION
    total_a_abonar = costo_total + comision_total
    print("El costo total de la publicacion es de:", costo_total)
    print("La comision es de: ", comision_total)
    print("El total a pagar es de:", total_a_abonar)