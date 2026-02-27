class Deseo: 
    def __init__(self,id, nombre, marca, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = int(cantidad)
        
    
    def toJson(self):
        return {"id":self.id, "nombre":self.nombre,"marca":self.marca,"descripcion":self.descripcion,"precio":self.precio,"cantidad":self.cantidad}