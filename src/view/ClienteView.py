from repository.ClienteRepository import  ClienteRepository


class ClienteView(object):
    
    def __init__(self, repo: ClienteRepository):
        """Constructor
            Initialize the repository
        Args:
            repo (ClienteRepository): objecct to data access
        """        
        self.repo = repo
    
    
    
    def show_all_clientes(self):
        """Method to show all clientes
        Returns:
            tuple: tuple with all clientes_
        """    
        return  self.repo.get_all()
    
    
    
    def get_cliente_by_param(self, param: int):
        """Method to get cliente by id
        Args:
            param (number): id of the client
        Returns:
            tuple: the unique tuple with information
        """        
        return  self.repo.find_by_id(param)
    
    
    
    
    
    
    def update_cliente(self, param):
        return  "update  cliente ......"
    
    def insert_cliente(self, param):
        return  "insert cliente ......"
    