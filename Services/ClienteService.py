class ClienteService:
    def __init__(self):
        self.clientes = []

    def PostCliente(self, nombre, email):
     id = len(self.clientes) + 1
     nuevoCliente = {
     "id" : id,
     "nombre":nombre,
     "email":email
     }
     self.clientes.append(nuevoCliente)
     print("\n=== Cliente creado exitosamente ===\n")

    def GetClientes(self):
     if self.clientes:
      print("\n=== Lista de Clientes ===\n")
      for cliente in self.clientes:
         print(f"Id: {cliente['id']}\nCliente: {cliente['nombre']}\nEmail: {cliente['email']}\n")
         print("==========")
     else:
        print("==========")
        print("\nNo hay clientes Registrados!\n")
        print("==========")

    def DeleteCliente(self, id):
      if self.clientes:
        for cliente in self.clientes:
          if cliente["id"] == id:
            self.clientes.remove(cliente)
            print(f"\nSe elimino El Cliente con ID: {id}\n")
        print(f"\nNo se encontro el ID: {id}\n")
