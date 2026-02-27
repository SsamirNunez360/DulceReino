class Proveedor:
    def __init__(self, id, nombre, email, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
    
    def toJson(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'direccion': self.direccion,
            'telefono': self.telefono
        }