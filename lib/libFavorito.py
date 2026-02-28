from lib.favorito import Favorito
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LibFavorito:
    
    def create(self,id, nombre, marca, precio, publico, fecha):
        persona = Favorito(id, nombre, marca, precio, publico, fecha)
        file = open(os.path.join(BASE_DIR, "data/favorito.json"))
        j = json.load(file)
        j = j + [persona.toJson()]
        file = open(os.path.join(BASE_DIR, "data/favorito.json"),"w")
        json.dump(j,file,ensure_ascii=False, indent=4)
        file.close()
        return True
    
    def get_favorito(self):
        file = open(os.path.join(BASE_DIR, "data/favorito.json"))
        j = json.load(file)
        list = []
        for x in j:
            list.append(Favorito(x['id'],x['nombre'],x['marca'],x['precio'],x['publico'],x['fecha']))
        return list 
    
    def get_favorito_by_id(self, id):
        file = open(os.path.join(BASE_DIR, "data/favorito.json"))
        j = json.load(file)
        for x in j: 
            if(x['id']==id):
                return Favorito(x['id'],x['nombre'],x['marca'],x['precio'],x['publico'],x['fecha'])
        return None
    
    def edit_favorito(self,id, nombre, marca, precio, publico, fecha):
        file = open(os.path.join(BASE_DIR, "data/favorito.json"))
        j = json.load(file)
        for x in j: 
            if(x['id']==id):
                x['nombre'] = nombre
                x['marca']= marca
                x['precio']= precio
                x['publico']= publico
                x['fecha']= fecha
                file = open(os.path.join(BASE_DIR, "data/favorito.json"),"w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    
    def eliminar(self, id):
        file = open(os.path.join(BASE_DIR, "data/favorito.json"))
        j = json.load(file)
        for i in range(0,len(j)): 
            if(j[i]['id']==id):
                j = j[:i]+ j[i+1:]
                file = open(os.path.join(BASE_DIR, "data/favorito.json"),"w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False


