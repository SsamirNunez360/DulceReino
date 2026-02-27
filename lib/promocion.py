class Promocion:
    def __init__(self, codigo, nombre, descripcion, descuento, fechainicio, fechafinal):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.descuento = descuento
        self.fechainicio = fechainicio
        self.fechafinal = fechafinal

    def toJson(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "descuento": self.descuento,
            "fechainicio": self.fechainicio,
            "fechafinal": self.fechafinal,
        }
