from lib.resenia import Resenia
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data/resenias.json")


class LibResenia:

    def create(self, id, descripcion):
        resenia = Resenia(id, descripcion)

        with open(FILE_PATH, "r", encoding="utf-8") as file:
            j = json.load(file)

        j.append(resenia.toJson())

        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(j, file, ensure_ascii=False, indent=4)

        return True

    def get_resenia(self):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            j = json.load(file)

        lista = []
        for x in j:
            lista.append(Resenia(x['id'], x['descripcion']))

        return lista

    def get_resenia_by_id(self, id):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            j = json.load(file)

        for x in j:
            if x['id'] == id:
                return Resenia(x['id'], x['descripcion'])

        return None

    def edit_resenia(self, id, descripcion):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            j = json.load(file)

        for x in j:
            if x['id'] == id:
                x['descripcion'] = descripcion

                with open(FILE_PATH, "w", encoding="utf-8") as file:
                    json.dump(j, file, ensure_ascii=False, indent=4)

                return True

        return False

    def eliminar(self, id):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            j = json.load(file)

        for i in range(len(j)):
            if j[i]['id'] == id:
                j.pop(i)

                with open(FILE_PATH, "w", encoding="utf-8") as file:
                    json.dump(j, file, ensure_ascii=False, indent=4)

                return True

        return False