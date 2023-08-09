import uuid


class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self. email = email
        self. position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self) # chequea lo que devuelve el metodo __dict__ y permite aceder a un diccionario de nuestro objeto, para poder escribirloa a disco en csv
    
    @staticmethod
    def schema():
        return ['name', 'company', 'email', 'position', 'uid'] 