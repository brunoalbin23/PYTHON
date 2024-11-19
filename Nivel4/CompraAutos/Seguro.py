class Seguro:
    def __init__(self, id, tipo_seguro, precio):
        self.id = id
        self.tipo_seguro = tipo_seguro
        self.precio = precio

    def mostrar_informacion(self):
        return f"Seguro: {self.tipo_seguro} - Precio: ${self.precio}"
