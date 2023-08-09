from Services.ClienteService import ClienteService
 
class ClienteController:
    def __init__(self):
        self.clienteService = ClienteService()


    def crearCliente(self):
     nombre = input("Ingrese el nombre del Cliente: ")
     email = input("Ingrese el email del Cliente: ")

     self.clienteService.PostCliente(nombre, email)

    def listarClientes(self):
     self.clienteService.GetClientes()

    def deleteCliente(self):
       idToDelete = int(input("\nIngrese el Id a Eliminar\n"))
       if idToDelete:
        self.clienteService.DeleteCliente(idToDelete)
       else:
        print("Error al eliminar (No se encontro el Id)")

       