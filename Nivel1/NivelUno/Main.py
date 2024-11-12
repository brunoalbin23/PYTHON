import math


def contador_vocales(palabra):
    contador = 0
    for i in palabra:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            contador += 1
    return contador


def suma_rango(num):
    suma = 0
    for i in range(1, num + 1):
        suma += i
    return suma


def lista_cuadrados(num):
    for i in range(1, num + 1):
        print(f"El cuadrado de {i} es {i ** 2}")


def invertir_cadena(cadena):
    nueva_cadena = ""
    for i in range(len(cadena) - 1, -1, -1):
        nueva_cadena += cadena[i]
    return nueva_cadena


def suma_pares(num):
    suma = 0
    for i in range(2, num + 1):
        if i % 2 == 0:
            suma += i
    return suma


def contador_palabras(palabra):
    lista_palabras = palabra.split()
    return len(lista_palabras)


def devolver_mayor():
    a = int(input("Número A: "))
    b = int(input("Número B: "))
    c = int(input("Número C: "))
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


def repetidor_de_cadenas(cadena, cantidad):
    for i in range(1, cantidad):
        print(cadena)
    return ""


def ultimo_digito(num):
    return num % 10


def calcular_propina(monto, porcentaje):
    return monto * (porcentaje / 100)


def area_circulo(radio):
    return math.pi * (radio ** 2)


def invertir_numero(num):
    num_str = str(num)
    nuevo_num = ""
    for i in range(len(num_str) - 1, -1, -1):
        nuevo_num += num_str[i]
    return int(nuevo_num)


def centenas_decenas_unidades(num):
    cen = (num % 1000) // 100
    dec = (num % 100) // 10
    uni = num % 10
    print(f"Centenas: {cen}, Decenas: {dec}, Unidades: {uni}")


def anos_en_meses_dias(anos):
    meses = anos * 12
    dias = anos * 365
    print(f"Años: {anos}\nMeses: {meses}\nDias: {dias}")


def remplazo_vocales_caracter(cadena, caracterr):
    nueva_cadena = ""
    for i in cadena:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            nueva_cadena += caracterr
        else:
            nueva_cadena += i
    return nueva_cadena


def remplazo_vocales_contador(cadena):
    nueva_cadena = ""
    contador = 1;
    for i in cadena:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            nueva_cadena += str(contador)
            contador += 1
        else:
            nueva_cadena += i
    return nueva_cadena


# print(contador_vocales("jajaja todo bien?"))
# print(suma_rango(5))
# print(lista_cuadrados(6))
# print(invertir_cadena("esto deberia invertirse"))
# print(suma_pares(8))
# print(contador_palabras("aca deberia haber nueve palabras si no me equivoco"))
# devolver_mayor()
# print(repetidor_de_cadenas("hola jeje", 5))
# print(ultimo_digito(134276))
# print(calcular_propina(500, 15))
# print(area_circulo(4))
# print(invertir_numero(1234))
# centenas_decenas_unidades(123)
# anos_en_meses_dias(4)
# print(remplazo_vocales_caracter("cuando te veo, te veo pasarr aaaa nuu", "+"))
# print(remplazo_vocales_contador("probamos este a ver que saleee jaja dos"))