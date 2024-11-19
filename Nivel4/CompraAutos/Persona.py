from Patente import Patente
from Seguro import Seguro


class Persona:
    def __init__(self, nombre, cedula, telefono, dinero):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__telefono = telefono
        self.__dinero = dinero
        self.__autos = []
        self.__gastos = {}

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

    def comprar_auto(self, auto):
        if auto.costo < self.get_dinero():
            self.__autos.append(auto)
            self.__dinero -= auto.costo
            print(f"{self.__nombre} compró el vehiculo: {auto.marca} {auto.modelo}, que lo disfrutes!")
        else:
            print("Esta compra no es posible, dinero insuficiente")

    def patentar_auto(self, id_lib, padron, letras, numeros, precio): #Este método en si lo tendria que tener alguien que trabaje en el municipio, no tiene sentido que una persona elija el precio o números de una patente, pero para este ejemplo alcanza
        auto_patentado = False
        for auto in self.__autos:
            if id_lib == auto.id_libreta and auto.patente is None:
                if self.__dinero > precio:
                    patente = Patente(padron, letras, numeros, precio)
                    auto.patente = patente
                    self.__dinero -= precio
                    self.__gastos[patente.padron] = patente
                    auto_patentado = True
                    print(f"{self.__nombre} patentó su vechiculo con libreta: {id_lib} con la patente: {letras} {numeros} - costo: U$S {precio}")
                else:
                    print("No se puedo hacer la operación, dinero insuficiente")
        if not auto_patentado:
            print("No hay ningun auto para patentar con esa información disponible")

    def asegurar_auto(self, id_libreta, id_seguro, tipo_seguro, precio):
        auto_asegurado = False
        for auto in self.__autos:
            if id_libreta == auto.id_libreta and auto.seguro is None:
                if self.__dinero > precio:
                    seguro = Seguro(id_seguro, tipo_seguro, precio)
                    auto.seguro = seguro
                    self.__dinero -= precio
                    self.__gastos[seguro.id] = seguro
                    auto_asegurado = True
                    print(
                        f"{self.__nombre} aseguró su vechiculo con libreta: {id_libreta} con un seguro de tipo '{tipo_seguro}' - costo: U$S {precio}")
                else:
                    print("No se puedo hacer la operación, dinero insuficiente")
        if not auto_asegurado:
            print("No hay ningun auto para asegurar con esa información disponible")

    def mostrar_informacion(self):
        print(f"----INFORMACIÓN PERSONAL----\nNombre: {self.get_nombre()}, Cedula: {self.get_cedula()}, Télefono: {self.get_telefono()}, Dinero: {self.get_dinero()}\n----AUTOS EN PROPIEDAD----")
        if not self.__autos:
            print("Ninguno")
        for i in self.__autos:
            print(i.mostrar_informacion())
        print("----PATENTES/SEGUROS----")
        if not self.__gastos:
            print("Ninguno")
        for i in self.__gastos.values():
            print(i.mostrar_informacion())
