import random


def numeros_narcisistas(num):  #La suma de las cifras elevado al cubo es igual a al número
    lista_numeros_cumplen = []
    for i in range(1, num + 1):
        lista_numeros_numero = numeros_en_numero(i)
        suma = 0
        for j in lista_numeros_numero:
            suma += j ** 3
        if i == suma:
            lista_numeros_cumplen.append(i)
    return lista_numeros_cumplen


# Función que uso para calculas los números narcisistas
def numeros_en_numero(num):  # Devuelve una lista de los números que componen al número, 505 = [5,0,5]
    lista = []
    numero_str = str(num)
    for i in numero_str:
        lista.append(int(i))
    return lista


def fibonacci(num):  # resultado de Fibonacci del valor número n
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)


def imprimir_secuencia_fibonacci(num):  # resultado de Fibonacci del valor número n
    valor1 = 1
    valor2 = 1
    copia = 0
    contador = 1
    print(valor1, end=" ")
    if num - 1 > 1:
        while True:

            print(valor1, end=" ")
            copia = valor1
            contador += 1

            if contador == num:
                break

            valor2 = valor2 + valor1
            print(valor2, end=" ")
            valor1 = valor2 + valor1
            contador += 1

            if contador == num:
                break
    return " "


def adivinar_numero():
    numero = random.randint(1, 100)
    print(numero)
    opcion = 0
    contador = 0
    while opcion != numero:
        opcion = int(input("Ingrese un valor: "))
        contador += 1
        if numero > opcion:
            print(f"EL número es mayor a {opcion}")
        elif opcion > numero:
            print(f"EL número es menosr a {opcion}")
        else:
            print(f"Adivinaste!! la palabra era {opcion}, lo hiciste en {contador} intentos")


def contar_palabras(frase):
    palabras_cantidad = {}
    solo_palabras = frase.split()
    for i in solo_palabras:
        if i not in palabras_cantidad.keys():
            palabras_cantidad[i] = 1
        else:
            palabras_cantidad[i] += 1
    for i in palabras_cantidad:
        if palabras_cantidad[i] == 1:
            print(f"La palabra '{i}' está 1 vez")
        else:
            print(f"La palabra '{i}' está {palabras_cantidad[i]} veces")


def calcular_mediana(lista_nums):
    largo = len(lista_nums)
    lista_nums.sort()
    if len(lista_nums) % 2 == 0:
        return (lista_nums[int(largo / 2 - 1)] + lista_nums[int(largo / 2)]) / 2
    else:
        return lista_nums[int(largo / 2)]


def es_anagrama(frase1, frase2):
    letras1 = contar_caracteres(frase1)
    letras2 = contar_caracteres(frase2)
    return letras1 == letras2


def contar_caracteres(frase):
    caracteres_cantidad = {}
    for i in frase:
        if i not in caracteres_cantidad.keys():
            caracteres_cantidad[i] = 1
        else:
            caracteres_cantidad[i] += 1
    return caracteres_cantidad


def code_cesar(frase, desplazamiento):
    devolver = []
    for i in frase:
        devolver.append(i)
    contador = 0
    for i in range(desplazamiento, len(frase)):
        devolver[i] = frase[contador]
        contador += 1
    for i in range(0, desplazamiento):
        devolver[i] = frase[contador]
        contador += 1
    return ''.join(devolver)


def decode_cesar(frase, desplazamiento):
    devolver = []
    for i in frase:
        devolver.append(i)
    contador = desplazamiento * (-1)
    otro_conta = 0
    for i in range(0, desplazamiento * (-1) - 1):
        devolver[i] = frase[contador]
        contador += 1
    for i in range(desplazamiento * -1 - 1, len(frase)):
        devolver[i] = frase[otro_conta]
        otro_conta += 1
    return ''.join(devolver)


def factores_primos(num):
    primos = numeros_primos(num)
    lista_factores = []
    while True:
        for i in primos:
            if num % i == 0:
                num = num // i
                lista_factores.append(i)
                break
        if num == 1:
            break
    return lista_factores


def numeros_primos(num):
    primos = []
    if num >= 2:
        primos.append(2)
    for i in range(3, num + 1):
        es_primo = True
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos


# print(numeros_narcisistas(500))
# print(fibonacci(8))  # 1 1 2 3 5 8 13 21
# print(imprimir_secuencia_fibonacci(8))
# adivinar_numero()
# contar_palabras("hola como estas amigo amigo estas hola como jaja hola jaja ja hola como estas hola ja")
# print(calcular_mediana([25,6,33,4,12,5]))
# print(es_anagrama("hla coomlo aeennndals","hola cllomo annenedas"))
# print(code_cesar("vamos a hacer de cuenta que esto es una frase super mega ñaa dificl", 22))
# print(decode_cesar(" super mega ñaa dificlvamos a hacer de cuenta que esto es una frase", -22))
# print(factores_primos(60))