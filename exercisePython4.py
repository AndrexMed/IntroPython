USERS = [
    {
        "idEmpleado": 1,
        "UserName": "GiAn",
        "NombreCompleto": "Giovanni Andres",
        "Clave": "123",
        "Salario": 500,
        "Rol": "Empleado"
    }
]

def printColilla(user):
    total = 0
    auxTransporte = 100
    numFactura = 0
    if user["Salario"] < 2000000:
        total = auxTransporte + user["Salario"]
        print("Nombre Completo: ", user["NombreCompleto"])
        print("Rol: ", user["Rol"])
        print("Salario Neto: ", user["Salario"])
        print("Total a pagar + aux: ", total)
    else:
        pass

def empleadoLogin(user):
    while True:
        print("1. Ver colilla")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            print("Entro a ver colilla")
            printColilla(user)
        elif opcion == 2:
            print("Good Bye")
            break
        else:
            print("Opcion invalida!")
    

def checkUser(usuario,passw):
    for user in USERS:
        if user["UserName"] == usuario and user["Clave"] == passw:
            return user
    return False

def menuEmpleado():
    print("\n *** Ingrese sus credenciales de acceso *** \n")
    usuario = input("Enter User Name: ")
    clave = input("Enter Password: ")
    userValid = checkUser(usuario,clave)
    if userValid:
        print("Usuario valido", userValid)
        empleadoLogin(userValid)
    else:
        print("Usuario invalido!")

def menuAnalista():
    pass

FLAG = True
while FLAG:
    print("1. Empleado")
    print("2. Analista de RH")
    opcion = int(input("Seleccione su Rol: "))

    if opcion == 1:
        menuEmpleado()
    elif opcion == 2:
        pass
    else:
        print("\n *** Opcion invalida ***\n")