from lib.proveedor import Proveedor
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LibProveedor:
    
    def __init__(self):
        # Asegurarse que el archivo y directorio existen
        os.makedirs("data", exist_ok=True)
        if not os.path.exists("data/proveedor.json"):
            with open(os.path.join(BASE_DIR, "data/proveedor.json"), "w") as f:
                json.dump([], f)
    
    def create(self, id, nombre, email, direccion, telefono):
        proveedor = Proveedor(id, nombre, email, direccion, telefono)
        with open(os.path.join(BASE_DIR, "data/proveedor.json"), "r+") as file:
            j = json.load(file)
            j.append(proveedor.toJson())
            file.seek(0)
            json.dump(j, file, ensure_ascii=False, indent=4)
        return True
    
    def get_proveedores(self):
        with open(os.path.join(BASE_DIR, "data/proveedor.json"), "r") as file:
            j = json.load(file)
            return [Proveedor(x['id'], x['nombre'], x['email'], x['direccion'], x['telefono']) for x in j]
    
    def get_proveedor_by_id(self, id):
        with open(os.path.join(BASE_DIR, "data/proveedor.json"), "r") as file:
            j = json.load(file)
            for x in j:
                if x['id'] == id:
                    return Proveedor(x['id'], x['nombre'], x['email'], x['direccion'], x['telefono'])
        return None
    
    def edit_proveedor(self,id, nombre, email, direccion, telefono):
        file = open(os.path.join(BASE_DIR, "data/proveedor.json"))
        j = json.load(file)
        for x in j: 
            if(x['id']==id):
                x['nombre'] = nombre
                x['email'] = email
                x['direccion']= direccion
                x['telefono']= telefono
                file = open(os.path.join(BASE_DIR, "data/proveedor.json"),"w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    
    def eliminar(self, id):
        with open(os.path.join(BASE_DIR, "data/proveedor.json"), "r+") as file:
            j = json.load(file)
            new_list = [x for x in j if x['id'] != id]
            
            if len(new_list) < len(j):  # Se eliminó un elemento
                file.seek(0)
                file.truncate()
                json.dump(new_list, file, ensure_ascii=False, indent=4)
                return True
        return False
    
    def search_by_nombre(self, nombre):
        with open(os.path.join(BASE_DIR, "data/proveedor.json"), "r") as file:
            j = json.load(file)
            return [Proveedor(x['id'], x['nombre'], x['email'], x['direccion'], x['telefono']) 
                    for x in j if nombre.lower() in x['nombre'].lower()]
    
    def search_by_email(self, email):
        with open(os.path.join(BASE_DIR, "data/proveedor.json"), "r") as file:
            j = json.load(file)
            return [Proveedor(x['id'], x['nombre'], x['email'], x['direccion'], x['telefono'])
                    for x in j if email.lower() in x['email'].lower()]