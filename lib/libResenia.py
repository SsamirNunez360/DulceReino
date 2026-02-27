from lib.resenia import Resenia
import json

class LibResenia:
    
    def create(self,id, descripcion):
        resenia = Resenia(id, descripcion)
        file = open("data/resenias.json")
        j = json.load(file)
        j = j + [resenia.toJson()]
        file = open("data/resenias.json","w")
        json.dump(j,file,ensure_ascii=False, indent=4)
        file.close()
        return True
    
    def get_resenia(self):
        file = open("data/resenias.json")
        j = json.load(file)
        list = []
        for x in j:
            list.append(Resenia(x['id'],x['descripcion']))
        return list 
    
    def get_resenia_by_id(self, id):
        file = open("data/resenias.json")
        j = json.load(file)
        for x in j: 
            if(x['id']==id):
                return Resenia(x['id'],x['descripcion'])
        return None
    
    def edit_resenia(self,id, descripcion):
        file = open("data/resenias.json")
        j = json.load(file)
        for x in j: 
            if(x['id']==id):
                x['descripcion'] = descripcion
                file = open("data/resenias.json","w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    
    def eliminar(self, id):
        file = open("data/resenias.json")
        j = json.load(file)
        for i in range(0,len(j)): 
            if(j[i]['id']==id):
                j = j[:i]+ j[i+1:]
                file = open("data/resenias.json","w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    