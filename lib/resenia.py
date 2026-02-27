class Resenia: 
    def __init__(self,id, descripcion):
        self.id = id
        self.descripcion = descripcion
    
    def toJson(self):
        return {"id":self.id,"descripcion":self.descripcion}