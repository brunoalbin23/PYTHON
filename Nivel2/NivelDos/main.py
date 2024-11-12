def esPalindromo(frase):
    contador = -1
    for i in frase:
        if i != frase[contador]:
            return False
        contador -= 1
    return True


def eliminar_duplicados(lista):
    return list(set(lista))


def factorial_recursivo(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursivo(num - 1)


def suma_digitos(num):
    digitos = str(num)
    suma = 0
    for i in digitos:
        suma += int(i)
    return suma


print(esPalindromo("ala"))
print(eliminar_duplicados(["apple", "banana", "cherry", "cherry", "pera", "banana", "anana"]))
print(factorial_recursivo(5))
print(suma_digitos(5465))
