class Patente:
    def __init__(self, padron, letras, numeros, precio):
        self.padron = padron
        self.letras = letras
        self.numeros = numeros
        self.precio = precio

    def mostrar_informacion(self):
        return f"Patente: {self.letras} {self.numeros} - Padron: {self.padron} - Precio: ${self.precio}"
