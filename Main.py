from Controller.ClienteController import ClienteController

clienteController = ClienteController()
flag = True
admin_name = "ElGio"

while flag:
    print(f"==== Hola {admin_name} ====")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    print("==============")
    opcion = int(input("\nIngrese una opción: \n"))

    if opcion == 1:
        clienteController.crearCliente()
    elif opcion == 2:
        clienteController.listarClientes()
    elif opcion == 3:
        pass
    elif opcion == 4:
        clienteController.deleteCliente()
    elif opcion == 5:
        print("\nGood Bye\n")
        flag = False