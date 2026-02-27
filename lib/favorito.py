class Favorito: 
    def __init__(self,id, nombre, marca, precio, publico, fecha):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.publico = publico
        self.fecha = fecha
        
    
    def toJson(self):
        return {"id":self.id, "nombre":self.nombre,"marca":self.marca,"precio":self.precio, "publico":self.publico, "fecha":self.fecha}