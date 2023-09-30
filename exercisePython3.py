numeroVentas = 0
totalVentas = 0

def imprimirDatos(subtotal, descuento, iva, total):
    print("Subtotal: ", subtotal)
    print("Descuento: ", descuento)
    print("Iva: ", iva)
    print("Total: ", total)

def imprimirResultados():
    if (totalVentas and numeroVentas) == 0:
        print("No hay ventas registradas")
    else:
        print("Total de ventas: ", totalVentas)
        print("Numero de ventas: ", numeroVentas)

def calcular(precio,cantidad):

    print("entro a calcular")
    subtotal = precio * cantidad
    descuento = subtotal * 0.10
    iva = subtotal * 0.19
    total = (subtotal - descuento) + iva

    global totalVentas, numeroVentas

    totalVentas += total
    numeroVentas += 1

    print("\nFactura registrada con exito!\n")

    imprimirDatos(subtotal, descuento, iva, total)

def Hello():
    codigoProducto = input("\nIngrese el codigo del producto\n")
    nombreProducto = input("\nIngrese el nombre del producto\n")
    precioProducto = float(input("\nIngrese el precio del producto\n"))
    cantidadProducto = int(input("\nIngrese el cantidad del producto\n"))

    if (precioProducto and cantidadProducto) <= 0:
        print("Precio y cantidad no pueden ser menor que 0")
    else:
        calcular(precioProducto, cantidadProducto)
#----------------------------------------------------------------------------------    
BANDERA = True
while BANDERA:
    print("1. Registrar factura")
    print("2. Salir")
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion == 1:
        Hello()
    elif opcion == 2:
        print("\nGood bye\n")
        imprimirResultados()
        BANDERA = False
    else:
        print("\nOpcion equivocada\n")
        