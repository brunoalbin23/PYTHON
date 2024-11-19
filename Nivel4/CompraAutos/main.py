from Persona import Persona
from Auto import Auto

persona1 = Persona("Bruno", 56315544, 91697659, 300000)
persona2 = Persona("Santi", 55555555, 99999999, 0)
persona3 = Persona("Pedro", 44444444, 98888888, 1000000)
persona4 = Persona("Rocio", 33333333, 97777777, 100000)

camaro = Auto("Chevrolet", "Camaro",1111,99000)
mustang = Auto("Ford", "Mustang", 2222, 84000)
raptor = Auto("Ford", "Ranger Raptor", 3333, 110000)
saveiro = Auto("Volkswagen", "Saveiro", 4444, 19000)
hilux = Auto("Toyota", "Hilux", 5555, 60000)
suzuki_alto = Auto("Suzuki", "Alto", 6666, 9900)

persona3.comprar_auto(raptor)
persona3.comprar_auto(mustang)
persona3.patentar_auto(2222, 9090, "LGA", 1234, 500)
persona3.asegurar_auto(2222, 1212, "CONTRA TODO", 1000)

print()
persona3.mostrar_informacion()