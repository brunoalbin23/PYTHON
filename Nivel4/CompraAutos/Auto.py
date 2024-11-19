class Auto:
    def __init__(self, marca, modelo, id_libreta, costo):
        self.marca = marca
        self.modelo = modelo
        self.id_libreta = id_libreta
        self.costo = costo
        self.dueño = None
        self.patente = None
        self.seguro = None

    def mostrar_informacion(self):
        return f"AUTO: Marca: {self.marca}, Modelo: {self.modelo}, Libreta: {self.id_libreta}, Precio: U$S {self.costo}"
