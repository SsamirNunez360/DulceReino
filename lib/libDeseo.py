from lib.deseo import Deseo
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LibDeseo:
    
    def create(self,id, nombre, marca, descripcion, precio, cantidad):
        persona = Deseo(id, nombre, marca, descripcion, precio, cantidad)
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"))
        j = json.load(file)
        j = j + [persona.toJson()]
        file = open(os.path.join(BASE_DIR, "data/dulce.json"),"w")
        json.dump(j,file,ensure_ascii=False, indent=4)
        file.close()
        return True
    
    def get_producto(self):
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"))
        j = json.load(file)
        list = []
        for x in j:
            list.append(Deseo(x['id'],x['nombre'],x['marca'],x['descripcion'],x['precio'], int(x['cantidad'])))
        return list 
    
    def get_dulce_by_id(self, id):
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"))
        j = json.load(file)
        for x in j: 
            if(x['id']==id):
                return Deseo(x['id'],x['nombre'],x['marca'],x['descripcion'],x['precio'],int(x['cantidad']))
        return None
    
    def edit_dulce(self,id, nombre, marca, descripcion, precio, cantidad):
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"))
        j = json.load(file)
        for x in j: 
            if(x['id']==id):
                x['nombre'] = nombre
                x['marca']= marca
                x['descripcion'] = descripcion
                x['precio']= precio
                x['cantidad']= cantidad
                file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"),"w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    
    def eliminar(self, id):
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"))
        j = json.load(file)
        for i in range(0,len(j)): 
            if(j[i]['id']==id):
                j = j[:i]+ j[i+1:]
                file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"),"w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    

    def search_by_name(self, name):
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"), "r")
        j = json.load(file)
        file.close()
        results = [Deseo(x['id'], x['nombre'], x['marca'], x['descripcion'], x['precio'],  int(x['cantidad'])) 
                for x in j if name.lower() in x['nombre'].lower()]
        return results
    
    def search_by_marca(self, marca):
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"), "r")
        j = json.load(file)
        file.close()
        results = [Deseo(x['id'], x['nombre'], x['marca'], x['descripcion'], x['precio'], int(x['cantidad']))
                for x in j if marca.lower() in x['marca'].lower()]
        return results
    
    def comprar_dulce(self, id):
        file = open(os.path.join(BASE_DIR, "data/lista_deseo.json"), "r")
        j = json.load(file)
        file.close()
        for x in j:
            if x['id'] == id:
                cantidad = int(x['cantidad']) 
                if cantidad > 0:
                    x['cantidad'] = cantidad - 1
                    with open(os.path.join(BASE_DIR, "data/lista_deseo.json"), "w") as file:
                        json.dump(j, file, ensure_ascii=False, indent=4)
                    return True  
                else:
                    return False 
        return False  