class Persona:
    def __init__(self, nombre, cedula, telefono, dinero):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__telefono = telefono
        self.__dinero = dinero
        self.__autos = []

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_telefono(self):
        return self.__telefono

    def get_dinero(self):
        return self.__dinero

    def get_autos(self):
        return self.__autos

    def aumentar_dinero(self, dinero):
        self.__dinero += dinero

