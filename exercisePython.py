
totalPersonasGuajira = 0
totalPersonasChicamocha = 0
totalPersonasLlanos = 0

totalDineroGuajira = 0
totalDineroChicamocha = 0
totalDineroLlanos = 0

sumaTotalTodosLosDestinos = 0

nombreDestino = ""

# ---------------------------------------------------------------------------------------------------
def imprimirTodasLasCotizaciones():
    sumaTotalDineroGuajira = "{:,}".format(totalDineroGuajira)
    sumaTotalDineroChicamocha = "{:,}".format(totalDineroChicamocha)
    sumaTotalDineroLlanos = "{:,}".format(totalDineroLlanos)
    sumaTotalTodosLosDestinos_format = "{:,}".format(sumaTotalTodosLosDestinos)

    print("\n*** Resultado de todas las cotizaciones ***\n")
    print("Total personas Guajira: ", totalPersonasGuajira)
    print("Total personas Chicamocha: ", totalPersonasChicamocha)
    print("Total personas Llanos: ", totalPersonasLlanos)
    print("Total dinero Guajira", sumaTotalDineroGuajira)
    print("Total dinero Chicamocha: ", sumaTotalDineroChicamocha)
    print("Total dinero Llanos: ", sumaTotalDineroLlanos)
    print("Total dinero TODOS LOS DESTINOS: ", sumaTotalTodosLosDestinos_format)
# ---------------------------------------------------------------------------------------------------
def imprimirResultadosDeCotizacion(nombreCliente, nombreDestino, totalAdultos, totalNiños, subtotal):
    subtotal_format = "{:,}".format(subtotal)

    print("\n*** Datos de la cotizacion ***\n")
    print("Nombre del cliente: ", nombreCliente)
    print("Lugar de destino: ", nombreDestino)
    print("Total adultos: ", totalAdultos)
    print("Total niños: ", totalNiños)
    print("Subtotal: ", subtotal_format , "\n")
    print("==========================================")
# ---------------------------------------------------------------------------------------------------
def realizarCalculosDeCotizacion(nombreCliente, numAdultos, numNiños, lugarDestino):
    global totalPersonasGuajira, totalPersonasChicamocha, totalPersonasLlanos, nombreDestino, totalDineroGuajira, totalDineroChicamocha, totalDineroLlanos, sumaTotalTodosLosDestinos

    totalPersonas = numAdultos + numNiños
    precioPorAdulto = 0
    precioPorNiño = 0

    if lugarDestino == 1:
        precioPorAdulto = 1450000
        precioPorNiño = 870000
        totalPersonasGuajira += totalPersonas
        nombreDestino = "Guajira"
    elif lugarDestino == 2:
        precioPorAdulto = 1600000
        precioPorNiño = 960000
        totalPersonasChicamocha += totalPersonas
        nombreDestino = "Cañon de Chicamocha"
    elif lugarDestino == 3:
        precioPorAdulto = 1200000
        precioPorNiño = 720000
        totalPersonasLlanos += totalPersonas
        nombreDestino = "Llanos orientales"
    
    subtotal = (precioPorAdulto * numAdultos) + (precioPorNiño * numNiños)
    sumaTotalTodosLosDestinos += subtotal

    if lugarDestino == 1:
        totalDineroGuajira += subtotal
    elif lugarDestino ==2:
        totalDineroChicamocha += subtotal
    elif lugarDestino == 3:
        totalDineroLlanos += subtotal

    imprimirResultadosDeCotizacion(nombreCliente, nombreDestino, numAdultos, numNiños, subtotal)

# ---------------------------------------------------------------------------------------------------
def datosIngreso():
    nombreCliente = input("Ingrese el nombre del Cliente: ")
    numAdultos = int(input("Ingrese el numero de adultos: "))
    numNiños = int(input("Ingrese el numero de niños: "))
    lugarDestino = int(input("\nIngrese el lugar de Destino:\n1. Guajira\n2. Cañon Chicamocha\n3.Llanos Orientales\n"))
    realizarCalculosDeCotizacion(nombreCliente, numAdultos, numNiños, lugarDestino)

# ---------------------------------------------------------------------------------------------------
flag = True

while flag:
    print("\n<== Sistema de Cotizacion ==>\n")
    print("1. Realizar Cotizacion.")
    print("2. Resultado de todas las cotizaciones.")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion.\n"))

    if opcion == 1:
        datosIngreso()
    elif opcion == 2:
        imprimirTodasLasCotizaciones()
    elif opcion == 3:
        print("\n*** Good Bye ***\n")
        flag = False