
#import  model.Cliente as Cliente
#from model.Cliente import Cliente

from model.Cliente import Cliente
from view.ClienteView import ClienteView
from repository.ClienteRepository import ClienteRepository  


class ClienteController(object):
    
    def __init__(self, cliente : Cliente, view : ClienteView) :
        """ Constructor
            Initialize the  View an d the Model 
            is possible to change  the constructor to receive  inyection of dependencies 
        """        
        self.cliente = cliente
        self.view = view
       
    
    def show_all_clientes(self):
        """Method to get all clientes
        Returns:
            tuple: with all information about clientes
        """        
        return self.view.show_all_clientes()
    
    
    def  find_cliente_by_id(self, cliente_id: int):
        """Method to find a client by id
        Args:
            cliente_id (_type_): id cliente

        Returns:
            _type_: _description_
        """    
        return self.view.get_cliente_by_param(cliente_id)
    
    
    
    
   
   



