from lib.promocion import Promocion
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LibPromocion:

    def create(self, codigo, nombre, descripcion, descuento, fechainicio, fechafinal):
        promocion = Promocion(codigo, nombre, descripcion, descuento, fechainicio, fechafinal)
        try:
            file = open(os.path.join(BASE_DIR, "data/promocion.json"), "r", encoding="utf-8")
            j = json.load(file)
            file.close()
        except:
            j = []
        
        j.append(promocion.toJson())

        file = open(os.path.join(BASE_DIR, "data/promocion.json"), "w", encoding="utf-8")
        json.dump(j, file, ensure_ascii=False, indent=4)
        file.close()
        return True

    def get_promociones(self):
        file = open(os.path.join(BASE_DIR, "data/promocion.json"), "r", encoding="utf-8")
        j = json.load(file)
        file.close()
        lista = []
        for x in j:
            lista.append(Promocion(x['codigo'], x['nombre'], x['descripcion'], x['descuento'], x['fechainicio'], x['fechafinal']))
        return lista

    def eliminar(self, nombre):
        file = open(os.path.join(BASE_DIR, "data/promocion.json"), "r", encoding="utf-8")
        j = json.load(file)
        file.close()

        for i in range(len(j)):
            if j[i]['nombre'] == nombre:
                j = j[:i] + j[i+1:]
                file = open(os.path.join(BASE_DIR, "data/promocion.json"), "w", encoding="utf-8")
                json.dump(j, file, ensure_ascii=False, indent=4)
                file.close()
                return True
        return False