import sys
from controller.ClienteController import ClienteController
from model.Cliente import Cliente
from view.ClienteView import ClienteView
from repository.ClienteRepository import ClienteRepository

#for p in sys.path:
#    print(p)
#print("VERSION....", sys.version)
#for p in sys.modules:
#    print(p)

#INIT MODEL
cliente = Cliente()
cliente.nb_nombre="mauricio"
cliente.nb_ap_paterno="londono"

#INIT REPOSITORY
repo = ClienteRepository()

#INIT VIEW
view = ClienteView(repo)

#INIT CONTROLLER
control = ClienteController(cliente,view)
res1 = control.show_all_clientes()
print("GET ALL CLIENTES`")
print(res1)


res2 = control.find_cliente_by_id(1)
print("GET CLIENTE by ID`")
print(res2)


    

   